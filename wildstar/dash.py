from lib.pybot.pybot import activate_window, sleep, send, single_instance, wait, \
    add_hotkey_double
from wildstar.util import *

coords = [None, None]
win_name = 'WildStar 16042'

sleep(2000)

activate_window(win_name)

@single_instance
def dash(key):
    if key == 's':
        if skill_f3():
            send('f3', 4)
            return
        if skill_f2():
            send('f2', 4)
            return
    if key == 'a' or key =='d':
        if skill_f2():
            send('f2', 4)
            return

add_hotkey_double('a', dash, ('a',), timeout=200)
add_hotkey_double('s', dash, ('s',), timeout=200)
add_hotkey_double('d', dash, ('d',), timeout=200)

wait('ctrl+q', exit, (0))
