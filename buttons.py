from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


test1 = KeyboardButton(text="Бренд")
test2 = KeyboardButton(text="Название")
test3 = KeyboardButton(text="Описание")
test4 = KeyboardButton(text="Цена")
test5 = KeyboardButton(text="Фото")
test6 = KeyboardButton(text="Оставить анкету такой")

testbtn = ReplyKeyboardMarkup(keyboard=[
    [test1, test2],
    [test3, test4],
    [test5, test6]
], resize_keyboard=True)