import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile
from aiogram.filters.command import Command

from data import *
from secret import token
from buttons import testbtn

import asyncio
import logging


PHOTOS_DIR = '.cache'


logging.basicConfig(level=logging.INFO)
bot = Bot(token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Здравствуйте напишите бренд")


@dp.message(F.text)
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

    elif text == "Бренд":
        await set_lastchm(id, text)
        await bot.send_message(id, "Напиши бренд")

    elif text == "Название":
        await set_lastchm(id, text)
        await bot.send_message(id, "Напиши название")

    elif text == "Описание":
        await set_lastchm(id, text)
        await bot.send_message(id, "Напиши описание")

    elif text == "Цена":
        await set_lastchm(id, text)
        await bot.send_message(id, "Напиши цену")

    elif text == "Фото":
        await set_lastchm(id, text)
        await bot.send_message(id, "Пришли нью фоточкэ")

    else:
        await changes(id, text, message)
    
    


@dp.message(F.photo)
async def download_photo(message: types.Message):
    id = message.from_user.id
    photo = message.photo[-1]
    dest = f"tmp/{photo.file_id}.jpg"

    link = await get_photo(id)
    if link != None:
        os.remove(link)

    await bot.download(
        file=photo,
        destination=dest,
    )

    await set_photo(id, dest)
    text = await Announc(get_brand(id), get_name(id), get_overview(id), get_price(id))
    photo_file = FSInputFile(dest)
    await message.answer_photo(photo=photo_file, reply_markup=testbtn,caption=text)
    await get_lastchm(id)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
