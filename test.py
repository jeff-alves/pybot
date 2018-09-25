import timeit
import win32gui, win32ui, win32con, win32api

import time
from win32com import client
from pynput.mouse import Button, Controller as M_Controller
from pynput.keyboard import Key, Controller as K_Controller
from lib.pybot.pybot import imageSearch, loadTemplate, pixelSearch

gemia = loadTemplate('gemia22.png')
coords = [None, None]
if imageSearch(gemia, coords, 950,440,1920,1080):
    print(coords)

print(pixelSearch('#272923', 600, 600, 1))



# s1 = _screencap(950,440,1920,1080)
# s5 = _screencap5(950,440,1920,1080)
# cv.imshow('window1', s1)
# cv.imshow('window5', s5)
# cv.waitKey()

# sec = 3.0
# fps = 0.0
# a = None
# last_time = time.time()
# while time.time() - last_time < sec:
#     a = _screencap5(950,440,1920,1080)
#     fps += 1
# print(fps/sec)
# sec = 3.0
# fps = 0.0
# a = None
# last_time = time.time()
# while time.time() - last_time < sec:
#     a = _screencap(950,440,1920,1080)
#     fps += 1
# print(fps/sec)

# shell = client.Dispatch("WScript.Shell")
# # shell.Run("notepad.exe")
# shell.AppActivate("Sem título - Bloco de notas")
#
# keyboard = K_Controller()
# mouse = M_Controller()

# print('The current pointer position is {0}'.format(mouse.position))
# mouse.position = (600,600)
# print('Now we have moved it to {0}'.format(mouse.position))
# mouse.move(5, -5)
# mouse.press(Button.left)
# mouse.release(Button.left)
# mouse.move(5, -5)
# mouse.click(Button.left, 2)
# mouse.scroll(0, 2)

# keyboard.press(Key.space)
# keyboard.release(Key.space)
#
# keyboard.press('a')
# keyboard.release('a')
#
# keyboard.press('A')
# keyboard.release('A')
#
# with keyboard.pressed(Key.shift):
#     keyboard.press('b')
#     keyboard.release('b')
#
# keyboard.type('Hello World')


# def wrapper(func, *args, **kwargs):
#     def wrapped():
#         return func(*args, **kwargs)
#     return wrapped
#
# print(getPixel(1825,1014))
# print(getPixel2(1825,1014))
#
# wrapped = wrapper(getPixel, 600, 600)
# print(timeit.timeit(wrapped, number=300))
#
# wrapped = wrapper(getPixel2, 600, 600)
# print(timeit.timeit(wrapped, number=300))
#
# sec = 3.0
# fps = 0.0
# a = None
# last_time = time.time()
# while time.time() - last_time < sec:
#     a = getPixel(950,440)
#     fps += 1
# print(fps/sec)
# sec = 3.0
# fps = 0.0
# a = None
# last_time = time.time()
# while time.time() - last_time < sec:
#     a = getPixel2(950,440)
#     fps += 1
# print(fps/sec)


# tmp = win32gui.GetCursorPos()
# print(tmp)

# click(600, 600)