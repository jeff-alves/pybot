from lib.pybot.pybot import activate_window, sleep, send, single_instance, wait, \
    add_hotkey
from wildstar.util import *

coords = [None, None]
win_name = 'WildStar 16042'

sleep(2000)

activate_window(win_name)

def atacar():
    while em_batalha():
        if resc_5() and skill_f1():
            send('f1', 2)
        if skill_f4():
            if not hp_70():
                send('f4')
            elif not buff_cura():
                send('f4')
        if skill_r():
            send('r')
        if skill_2():
            send('2')
        if resc_5() and skill_f1():
            send('f1', 2)
        if skill_3():
            send('3')
        if skill_4():
            send('4')
        if resc_5() and skill_f1():
            send('f1', 2)
        if skill_1():
            send('1')

@single_instance
def auto_fight():
    for _ in range(15):
        if em_batalha():
            atacar()
            send('f')
            break
        else:
            sleep(150)


add_hotkey('1', auto_fight, ())
wait('ctrl+q', exit, (0))
