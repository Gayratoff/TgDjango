from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

from loader import db


index = 0
keys = []
K = 0
menu = db.select_all_menu()
for x in menu:
    menu_turi = x[1]
    if K % 2 == 0 and K != 0:
        index += 1
    if K % 2 == 0:
        keys.append([KeyboardButton(text=f"{menu_turi}", )])
    else:
        keys[index].append(KeyboardButton(text=f"{menu_turi}", ))
    K+=1
# keys.append([KeyboardButton(text="Orqaga")])
menu_button = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)