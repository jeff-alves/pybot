#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import threading

import keyboard
import mouse
import cv2 as cv
import numpy as np
import winsound
import ctypes as ct

import time

from keyboard import KEY_UP
from mss import mss
sct = mss()

EnumWindows = ct.windll.user32.EnumWindows
EnumWindowsProc = ct.WINFUNCTYPE(ct.c_bool, ct.POINTER(ct.c_int), ct.POINTER(ct.c_int))
GetWindowText = ct.windll.user32.GetWindowTextW
GetWindowTextLength = ct.windll.user32.GetWindowTextLengthW
IsWindowVisible = ct.windll.user32.IsWindowVisible


LAST_HOTKEY = None

# def update_last_key(ev):
#     global LAST_HOTKEY
#     LAST_HOTKEY = ev
#
# keyboard.hook(update_last_key)

def wait(hotkey=None, suppress=False, trigger_on_release=False):
    keyboard.wait(hotkey, suppress, trigger_on_release)

def sleep(ms):
    time.sleep(ms / 1000.)

def get_active_window_name():
    hwnd = ct.windll.user32.GetForegroundWindow()
    return get_window_title(hwnd)

def get_window_title(hwnd):
    length = GetWindowTextLength(hwnd)
    buff = ct.create_unicode_buffer(length + 1)
    GetWindowText(hwnd, buff, length + 1)
    return buff.value

def get_matching_windows(title_list):
    matches = {}
    def window_enum_callback(hwnd, lParam):
        if IsWindowVisible(hwnd):
            window_name = get_window_title(hwnd).lower()
            for name in title_list:
                if name not in window_name:
                    return True
            matches[window_name] = hwnd
        return True
    EnumWindows(EnumWindowsProc(window_enum_callback), 0)
    return matches

def activate_window(title):
    matches = get_matching_windows(title)
    if matches:
        for key in sorted(matches, key=len):
            ct.windll.user32.SetForegroundWindow(matches[key])
            return

def sound_beep(frequency=2000, duration=100):
    winsound.Beep(frequency, duration)

def send(key, count=1):
    for _ in range(count):
        keyboard.send(key)

def click(coords, count=1, button='left'):
    if count > 0:
        for _ in range(count):
            mouse.move(coords[0], coords[1], absolute=True, duration=0)
            mouse.click(button)
    else:
        mouse.move(coords[0], coords[1], absolute=True, duration=0)

def rgb2hex(r,g,b):
    return "0x{:02x}{:02x}{:02x}".format(r,g,b)

def hex2brg(hexcode):
    return [int(hexcode[2:][i:i + 2], 16) for i in (4, 2, 0)]

def _screencap(tl_x, tl_y, br_x, br_y):
    return cv.cvtColor(np.asarray(sct.grab((tl_x, tl_y, br_x+1, br_y+1))), cv.COLOR_BGRA2BGR)

def load_image(name):
    template = cv.imread(os.path.normpath(name), cv.IMREAD_UNCHANGED)
    if template.shape[2] > 3:
        channels = cv.split(template)
        mask = np.array(channels[3])
        return {'templ': cv.cvtColor(template, cv.COLOR_BGRA2BGR), 'mask': cv.cvtColor(mask, cv.COLOR_GRAY2BGR), 'method':cv.TM_SQDIFF}
    return {'templ': template, 'method':cv.TM_SQDIFF}

def load_pixel(color):
    pixel = np.zeros([1, 1, 3], dtype=np.uint8)
    pixel[0][0] = hex2brg(color)
    return {'templ': pixel, 'method':cv.TM_SQDIFF}

def image_search(template, tl_x, tl_y, br_x = None, br_y = None, coords=None, erro = 2):
    br_x = br_x or tl_x
    br_y = br_y or tl_y
    source = _screencap(tl_x, tl_y, br_x, br_y)
    res = cv.matchTemplate(source, **template)
    min_erro, max_val, tl, max_loc = cv.minMaxLoc(res)
    if min_erro <= erro:
        if coords:
            coords[0] = tl[0] + tl_x + int(template['templ'].shape[0]/2)
            coords[1] = tl[1] + tl_y + int(template['templ'].shape[1]/2)
        return True
    return False

def single_instance(function):
    lock = threading.Lock()
    def new_function(*args, **kwargs):
        if lock.acquire(False):
            try:
                r = function(*args, **kwargs)
            except Exception as e:
                raise e
            finally:
                lock.release()
            return r
    return new_function


def thread_func(f,a):
    threading.Thread(target=f, args=a).start()

def add_hotkey_combo(hotkey, callback, args=(), suppress=False, timeout=1, trigger_on_release=False, new_thread = True):
    if new_thread:
        keyboard.add_hotkey(hotkey, thread_func, (callback, args), suppress, timeout, trigger_on_release)
    else:
        keyboard.add_hotkey(hotkey, callback, args, suppress, timeout, trigger_on_release)

def add_hotkey(key, function, args = (), suppress=False, new_thread = True):
    if new_thread:
        keyboard.hook_key(key, lambda e: e.event_type == KEY_UP or thread_func(function, args), suppress=suppress)
    else:
        keyboard.hook_key(key, lambda e: e.event_type == KEY_UP or function(*args), suppress=suppress)

def double_check(ev, timeout, f, a, new_thread):
    global LAST_HOTKEY
    tmp = LAST_HOTKEY
    LAST_HOTKEY = ev
    if ev.event_type == 'down' and tmp and tmp.event_type == 'up' and tmp.scan_code == ev.scan_code and (ev.time - tmp.time) <= (timeout/1000):
        if new_thread:
            thread_func(f, a)
        else:
            f(*a)

def add_hotkey_double(key, function, args = (), timeout = 300, suppress = False, new_thread = True):
    # keyboard.hook_key(key, lambda e: e.event_type == KEY_UP or double_check(e, timeout, function, args, new_thread), suppress=suppress)
    keyboard.hook_key(key, lambda e: double_check(e, timeout, function, args, new_thread), suppress=suppress)
