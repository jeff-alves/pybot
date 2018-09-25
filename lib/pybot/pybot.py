#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
from mss import mss
sct = mss()

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)


def hex2rgb(hexcode):
    return tuple(int(hexcode[1:][i:i + 2], 16) for i in (0, 2, 4))

def _screencap(tl_x, tl_y, br_x, br_y):
    return cv.cvtColor(np.asarray(sct.grab((tl_x, tl_y, br_x, br_y))), cv.COLOR_BGRA2BGR)


def loadTemplate(name):
    template = cv.imread(name, cv.IMREAD_UNCHANGED)
    if template.shape[2] > 3:
        channels = cv.split(template)
        mask = np.array(channels[3])
        return {'templ': cv.cvtColor(template, cv.COLOR_BGRA2BGR), 'mask': cv.cvtColor(mask, cv.COLOR_GRAY2BGR), 'method':cv.TM_SQDIFF}
    return {'templ': template, 'method':cv.TM_SQDIFF}


def pixelSearch(hex_str, x, y, erro = 0):
    pix = sct.grab((x, y, x + 1, y + 1)).pixel(0,0)
    c = hex2rgb(hex_str)
    if erro:
        top = (pix[0] + erro, pix[1] + erro, pix[2] + erro)
        bot = (pix[0] - erro, pix[1] - erro, pix[2] - erro)
        if bot[0] <= c[0] <= top[0] and bot[1] <= c[1] <= top[1] and bot[2] <= c[2] <= top[2]:
            return True
        return False
    else:
        return pix == c


def imageSearch(template, coords, tl_x, tl_y, br_x, br_y, erro = 100):
    source = _screencap(tl_x, tl_y, br_x, br_y)
    res = cv.matchTemplate(source, **template)
    min_erro, max_val, tl, max_loc = cv.minMaxLoc(res)
    if min_erro <= erro:
        coords[0] = tl[0] + tl_x
        coords[1] = tl[1] + tl_y
        return True
    return False

#
# def GetWindowList():
#     top_windows = []
#     win32gui.EnumWindows(windowEnumerationHandler)
#     return top_windows
#
# def windowEnumerationHandler(hwnd, top_windows):
#     top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
#
#
# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#
# shell = client.Dispatch("WScript.Shell")
# shell.Run("notepad.exe")
# win32api.Sleep(200)
# shell.AppActivate("Sem título - Bloco de notas")
# win32api.Sleep(200)
# shell.SendKeys("%")
# win32api.Sleep(500)
# shell.SendKeys("t")
# win32api.Sleep(500)
# shell.SendKeys("r")
# win32api.Sleep(500)
# shell.SendKeys("name")
# win32api.Sleep(500)
# shell.SendKeys("{ENTER}")
#
# hwin = win32gui.GetDesktopWindow()
# width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
# height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
# left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
# top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
# hwindc = win32gui.GetWindowDC(hwin)
# srcdc = win32ui.CreateDCFromHandle(hwindc)
# memdc = srcdc.CreateCompatibleDC()
# bmp = win32ui.CreateBitmap()
# bmp.CreateCompatibleBitmap(srcdc, width, height)
# memdc.SelectObject(bmp)
# memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
# bmp.SaveBitmapFile(memdc, 'screenshot.bmp')
#
#
# tmp = win32gui.GetPixel(hwindc, 600, 600)
# print(tmp)
#
#
# tmp = win32gui.GetCursorPos()
# print(tmp)
#
# click(600, 600)
#
#
# results = []
# top_windows = []
# win32gui.EnumWindows(windowEnumerationHandler, top_windows)
# for i in top_windows:
#     if "notepad" in i[1].lower():
#         print(i)
#         win32gui.ShowWindow(i[0], 5)
#         win32gui.SetForegroundWindow(i[0])
#         break