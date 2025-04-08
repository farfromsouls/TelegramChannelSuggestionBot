from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import asyncio
import logging


logging.basicConfig(level=logging.INFO)
bot = Bot(token="7594575966:AAHFZnAmIR5cAWUYB-xCwSXxnsX5OcihonE")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("")

@dp.message()
async def handler(message: types.Message):

    id = message.from_user.id
    text = message.text

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())