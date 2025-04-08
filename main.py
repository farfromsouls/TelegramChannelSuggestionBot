# aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio
import logging



# keyboard buttons #1
test1 = KeyboardButton(text="")
test2 = KeyboardButton(text="")
test3 = KeyboardButton(text="")
test4 = KeyboardButton(text="")
test5 = KeyboardButton(text="")
test6 = KeyboardButton(text="")

main_btn = ReplyKeyboardMarkup(keyboard=[
    [test1, test2],
    [test3, test4],
    [test5, test6]
], resize_keyboard=True)



# connecting to "bot"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(START_MESSAGE)

# main handler
@dp.message()
async def handler(message: types.Message):

    id = message.from_user.id
    text = message.text

    await bot.send_message(id[0], text)




# start polling
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())