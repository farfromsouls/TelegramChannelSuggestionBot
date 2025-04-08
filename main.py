from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from data import *

import asyncio
import logging


logging.basicConfig(level=logging.INFO)
bot = Bot(token="7594575966:AAHFZnAmIR5cAWUYB-xCwSXxnsX5OcihonE")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Здравствуйте напишите бренд")


@dp.message()
async def handler(message: types.Message):
    id = message.from_user.id
    text = message.text

    if check_id(id) == 0:
        set_id(id)

    if get_lm(id) == None:
        await set_brand(id, text)
        await bot.send_message(id, "Напиши название чмо")
        await set_lm(id, "Напиши название чмо")
    elif get_lm(id) == "Напиши название чмо":
        await set_name(id, text)
        await bot.send_message(id, "Напиши описание чмо")
        await set_lm(id, "Напиши описание чмо")
    elif get_lm(id) == "Напиши описание чмо":
        await set_ove(id, text)
        await bot.send_message(id, "Напиши цену товара")
        await set_lm(id, "Напиши цену товара")
    elif get_lm(id) == "Напиши цену товара":
        await set_price(id, text)
        await bot.send_message(id, "Пришли фото хоточкэ :3 <3")
        await set_lm(id, "Пришли фото хоточкэ :3 <3")
    elif get_lm(id) == "Пришли фото хоточкэ :3 <3":
        pass


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())