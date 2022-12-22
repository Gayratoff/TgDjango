from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.menu import menu_button
from loader import dp,db,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    full_name = message.from_user.first_name
    user_id = message.from_user.id
    try:
        db.add_users(user_id=user_id, full_name=full_name)
    except Exception as xatolik:
        print(xatolik)
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_button)

@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Orqaga",reply_markup=menu_button)

menu = db.select_all_menu()
@dp.message_handler(text=[i[1] for i in menu])
async def bot_start(message: types.Message):
    message_txt= message.text
    tur_id = db.select_menu(nomi=message_txt)
    menu = db.select_maxsulot(tur_id=tur_id[0])
    index = 0
    keys = []
    K = 0
    print(menu)
    for x in menu:
        menu_turi = x[1]
        if K % 2 == 0 and K != 0:
            index += 1
        if K % 2 == 0:
            keys.append([KeyboardButton(text=f"{menu_turi}", )])
        else:
            keys[index].append(KeyboardButton(text=f"{menu_turi}", ))
        K += 1
    keys.append([KeyboardButton(text="Orqaga")])
    menu_button = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    await message.answer(f"Tanlang...",reply_markup=menu_button)

menular = db.select_all_maxsulot()
@dp.message_handler(text=[x[0] for x in menular])
async def bot_start(message: types.Message):
    nomi = message.text
    save = db.select_maxsulots(name=nomi)
    MNomi = save[1]
    rasm = save[4]
    narxi = save[2]
    tavsif = save[5]
    print(rasm)
    print(save)
    user = message.from_user.id
    await bot.send_photo(chat_id=user,photo=rasm,caption=f"Nomi: {MNomi}\n Narxi : {narxi}\n Malumot : {tavsif}")
