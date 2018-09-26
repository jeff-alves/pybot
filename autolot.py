from lib.pybot.pybot import activate_window, get_active_window_name, sleep, send, click
from util import *

coords = [None, None]
win_name = 'WildStar 16029'

activate_window(win_name)

while True:
    if get_active_window_name() == win_name:
        if tem_v():
            send('v')
        if not em_batalha():
            if chat_v(coords):
                click(coords)
                continue
            if chat_e(coords):
                click(coords)
                continue
            if chat_3(coords):
                click(coords)
                continue
            if tem_c():
                send('c')
                continue
    else:
        sleep(1000)
