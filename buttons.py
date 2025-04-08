from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


test1 = KeyboardButton(text="")
test2 = KeyboardButton(text="")
test3 = KeyboardButton(text="")
test4 = KeyboardButton(text="")
test5 = KeyboardButton(text="")
test6 = KeyboardButton(text="")

testbtn = ReplyKeyboardMarkup(keyboard=[
    [test1, test2],
    [test3, test4],
    [test5, test6]
], resize_keyboard=True)