import os
import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile
from aiogram.filters.command import Command

from data import *
from admin import *
from secret import *
from buttons import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Здравствуйте! Напишите бренд")


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
            ChatFullInfo = await bot.get_chat(new_request)
            ChatFullInfo =ChatFullInfo.username
            if ChatFullInfo == None:
                ChatFullInfo = 'Hidden'
            else:
                ChatFullInfo = '@' + ChatFullInfo

            caption = chanel_mes[0] + "\nПродавец:" + ChatFullInfo
            await bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=caption)

            await delete_user(new_request)
            os.remove(chanel_mes[1])
            await bot.send_message(new_request, "Ваша заявка принята!!! :)")

            if await get_alen_users() != 0:
                new_request = await check_bd()
                chanel_mes = await FirstTipochek(new_request)
                photo = FSInputFile(chanel_mes[1])
            
                await bot.send_photo(chat_id=admin_id, photo=photo, reply_markup=adminbtn, caption=chanel_mes[0])
                
        elif text == "❌":
            new_request = await check_bd()
            chanel_mes = await FirstTipochek(new_request)

            await delete_user(new_request)
            os.remove(chanel_mes[1])

            if await get_alen_users() != 0:
                new_request = await check_bd()
                chanel_mes = await FirstTipochek(new_request)
            await bot.send_message(new_request, "Ваша заявка отклонена!!! :(")
            
        return None
    

    lastm = await get_lm(id)

    # first try
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

    # changes
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
        await bot.send_message(id, "Ваша заявка обрабатывается",reply_markup=types.ReplyKeyboardRemove())
        
        await set_ia(id, 1)
        await set_ind(id)
        
        if await get_alen_users() == 1:
            photo_file = FSInputFile(await get_photo(id))
            brand = await get_brand(id)
            name = await get_name(id)
            overview = await get_overview(id)
            price = await get_brand(id)

            post = await Announc(brand, name, overview, price, True)
            photo_file = FSInputFile(await get_photo(id))

            await bot.send_photo(chat_id=admin_id, photo=photo_file, reply_markup=adminbtn, caption=post)

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
    photo_file = FSInputFile(await get_photo(id))
    brand = await get_brand(id)
    name = await get_name(id)
    overview = await get_overview(id)
    price = await get_brand(id)

    text = await Announc(brand, name, overview, price)
    photo_file = FSInputFile(dest)
    await message.answer_photo(photo=photo_file, reply_markup=userbtn, caption=text)
    await get_lastchm(id)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
