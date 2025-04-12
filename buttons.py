from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


brand = KeyboardButton(text="Бренд")
name = KeyboardButton(text="Название")
des = KeyboardButton(text="Описание")
price = KeyboardButton(text="Цена")
photo = KeyboardButton(text="Фото")
exit = KeyboardButton(text="Оставить анкету такой✅")

userbtn = ReplyKeyboardMarkup(keyboard=[
    [brand, name],
    [des, price],
    [photo, exit]
], resize_keyboard=True)

yes = KeyboardButton(text="✅")
no = KeyboardButton(text="❌")

adminbtn = ReplyKeyboardMarkup(keyboard=[
    [yes, no]
], resize_keyboard=True)