from lib.pybot.pybot import load_image, image_search, load_pixel

px_skill_1 = {
    'template':load_pixel('0xFFFFFF'),
    'tl_x': 728,
    'tl_y': 1048,
    'erro': 0
}

px_skill_2 = {
    'template':load_pixel('0xFFFFFF'),
    'tl_x': 787,
    'tl_y': 1048,
    'erro': 0
}

px_skill_3 = {
    'template':load_pixel('0xFFFFFF'),
    'tl_x': 844,
    'tl_y': 1048,
    'erro': 0
}

px_skill_4 = {
    'template':load_pixel('0xFFFFFF'),
    'tl_x': 903,
    'tl_y': 1048,
    'erro': 0
}

px_skill_f1 = {
    'template':load_pixel('0xFFFFFF'),
    'tl_x': 963,
    'tl_y': 1048,
    'erro': 0
}

px_skill_f2 = {
    'template':load_pixel('0xFFFFFF'),
    'tl_x': 1022,
    'tl_y': 1048,
    'erro': 0
}

px_skill_f3 = {
    'template':load_pixel('0xFFFFFF'),
    'tl_x': 1079,
    'tl_y': 1048,
    'erro': 0
}

px_skill_f4 = {
    'template':load_pixel('0xFFFFFF'),
    'tl_x': 1138,
    'tl_y': 1048,
    'erro': 0
}

px_skill_r = {
    'template':load_pixel('0xFFFFFF'),
    'tl_x': 661,
    'tl_y': 1048,
    'erro': 0
}

px_skill_x = {
    'template':load_pixel('0xFDFDFD'),
    'tl_x': 1255,
    'tl_y': 1041,
    'erro': 0
}

px_em_batalha = {
    'template':load_pixel('0x9CFF9C'),
    'tl_x': 915,
    'tl_y': 1070,
    'erro': 1
}

px_resc_5 = {
    'template':load_pixel('0xFBFFFF'),
    'tl_x': 960,
    'tl_y': 920,
    'erro': 0
}

px_resc_2 = {
    'template':load_pixel('0xFBFFFF'),
    'tl_x': 1060,
    'tl_y': 964,
    'erro': 5
}

px_hp_100_1 = {
    'template':load_pixel('0x30E4B3'),
    'tl_x': 708,
    'tl_y': 800,
    'erro': 10
}

px_hp_100_1 = {
    'template': load_pixel('0x30E4B3'),
    'tl_x':708,
    'tl_y':800,
    'erro': 10
}


px_hp_100_2 = {
    'template': load_pixel('0x7EC1A0'),
    'tl_x':708,
    'tl_y':800,
    'erro': 10
}

px_target_casting = {
    'template': load_pixel('0xF8E2D6'),
    'tl_x':1116,
    'tl_y':808,
    'br_x':1116,
    'br_y':812,
    'erro': 10
}

im_buff_cura = {
    'template':load_image('C:/Program Files/AutoHotkey/Scripts/wildstar/img/buff_cura.png'),
    'tl_x':498,
    'tl_y':694,
    'br_x':764,
    'br_y':738,
    'erro': 2
}

im_tem_c = {
    'template':load_image('C:/Program Files/AutoHotkey/Scripts/wildstar/img/c.png'),
    'tl_x':1125,
    'tl_y':660,
    'br_x':1183,
    'br_y':677,
    'erro': 2
}

im_tem_v = {
    'template':load_image('C:/Program Files/AutoHotkey/Scripts/wildstar/img/v.png'),
    'tl_x':1125,
    'tl_y':660,
    'br_x':1183,
    'br_y':677,
    'erro': 3
}

im_chat_v = {
    'template':load_image('C:/Program Files/AutoHotkey/Scripts/wildstar/img/chat_v.png'),
    'tl_x':1081,
    'tl_y':526,
    'br_x':1099,
    'br_y':724,
    'erro': 2
}

im_chat_e = {
    'template':load_image('C:/Program Files/AutoHotkey/Scripts/wildstar/img/chat_e.png'),
    'tl_x':1081,
    'tl_y':526,
    'br_x':1099,
    'br_y':724,
    'erro': 2
}

im_chat_3 = {
    'template':load_image('C:/Program Files/AutoHotkey/Scripts/wildstar/img/chat_3.png'),
    'tl_x':1081,
    'tl_y':526,
    'br_x':1099,
    'br_y':724,
    'erro': 2
}

im_buff_70_hp = {
    'template':load_image('C:/Program Files/AutoHotkey/Scripts/wildstar/img/buff_70_hp.png'),
    'tl_x':498,
    'tl_y':694,
    'br_x':764,
    'br_y':738,
    'erro': 2
}

def em_batalha():
    return image_search(**px_em_batalha)

def resc_2():
    return image_search(**px_resc_2)

def resc_5():
    return image_search(**px_resc_5)

def skill_1():
    return image_search(**px_skill_1)

def skill_2():
    return image_search(**px_skill_2)

def skill_3():
    return image_search(**px_skill_3)

def skill_4():
    return image_search(**px_skill_4)

def skill_f1():
    return image_search(**px_skill_f1)

def skill_f2():
    return image_search(**px_skill_f2)

def skill_f3():
    return image_search(**px_skill_f3)

def skill_f4():
    return image_search(**px_skill_f4)

def skill_r():
    return image_search(**px_skill_r)

def skill_x():
    return image_search(**px_skill_x)

def target_casting():
    return image_search(**px_target_casting)

def hp_100():
    return image_search(**px_hp_100_1) and image_search(**px_hp_100_2)

def hp_70():
    return image_search(**im_buff_70_hp)

def buff_cura(coords = None):
    return image_search(**im_buff_cura, coords = coords)

def tem_c():
    return image_search(**im_tem_c)

def tem_v():
    return image_search(**im_tem_v)

def chat_v(coords = None):
    return image_search(**im_chat_v, coords = coords)

def chat_e(coords = None):
    return image_search(**im_chat_e, coords = coords)

def chat_3(coords = None):
    return image_search(**im_chat_3, coords = coords)