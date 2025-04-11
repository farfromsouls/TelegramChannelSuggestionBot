import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile
from aiogram.filters.command import Command

from data import *
from admin import *
from secret import token, admin_id, CHAT_ID
from buttons import testbtn, adminbutt

import asyncio
import logging


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

    if await check_id(id) == 0:
        await set_id(id)

    if await get_ia(id) == 1:
        return None
    
    if id == admin_id:
        if text == "✅":
            new_request = await check_bd()
            chanel_mes = await FirstTipochek(new_request)
            photo = FSInputFile(chanel_mes[1])
            await bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=chanel_mes[0])
            await delete_user(new_request)
            os.remove(chanel_mes[1])

            if await get_alen_users() != 0:
                new_request = await check_bd()
                chanel_mes = await FirstTipochek(new_request)

        elif text == "❌":
            new_request = await check_bd()
            chanel_mes = await FirstTipochek(new_request)
            await delete_user(new_request)
            os.remove(chanel_mes[1])
            if await get_alen_users() != 0:
                new_request = await check_bd()
                chanel_mes = await FirstTipochek(new_request)
            
        else:
            return None
    
    lastm = await get_lm(id)
    if lastm == None:
        await set_brand(id, text)
        await bot.send_message(id, "Напишите название")
        await set_lm(id, "Напишите название")

    elif lastm == "Напишите название":
        await set_name(id, text)
        await bot.send_message(id, "Напишите описание")
        await set_lm(id, "Напишите описание")

    elif lastm == "Напишите описание":
        await set_ove(id, text)
        await bot.send_message(id, "Напишите цену")
        await set_lm(id, "Напишите цену")

    elif lastm == "Напишите цену":
        await set_price(id, text)
        await bot.send_message(id, "Пришлите фото")
        await set_lm(id, "Пришлите фото")

    elif text == "Бренд":
        await set_lastchm(id, text)
        await bot.send_message(id, "Напишите бренд")

    elif text == "Название":
        await set_lastchm(id, text)
        await bot.send_message(id, "Напишите название")

    elif text == "Описание":
        await set_lastchm(id, text)
        await bot.send_message(id, "Напишите описание")

    elif text == "Цена":
        await set_lastchm(id, text)
        await bot.send_message(id, "Напишите цену")

    elif text == "Фото":
        await set_lastchm(id, text)
        await bot.send_message(id, "Пришлите фото")

    elif text == "Оставить анкету такой✅":
        await bot.send_message(id, "Ваша заявка обрабатывается")
        await set_ia(id, 1)
        
        if await get_alen_users() == 1:
            post = await Announc(get_brand(id), get_name(id), get_overview(id), get_price(id), True)
            photo_file = FSInputFile(await get_photo(id))
            await bot.send_photo(chat_id=admin_id, photo=photo_file, reply_markup=adminbutt, caption=post)

    else:
        await changes(id, text, message)
    


@dp.message(F.photo)
async def download_photo(message: types.Message):
    id = message.from_user.id
    photo = message.photo[-1]
    dest = f"tmp/{photo.file_id}.jpg"

    if await get_ia(id) == 1:
        return None

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
    await message.answer_photo(photo=photo_file, reply_markup=testbtn, caption=text)
    await get_lastchm(id)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
