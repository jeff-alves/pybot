#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from lib.pybot.pybot import activate_window, get_active_window_name, sleep, send, click, single_instance, wait, \
    add_hotkey
from wildstar.util import *

coords = [None, None]
win_name = 'WildStar 16042'

sleep(2000)

activate_window(win_name)

@single_instance
def auto_loot():
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
            sleep(100)
        else:
            sleep(500)


add_hotkey('-', auto_loot, ())

wait('ctrl+q', exit, (0))
