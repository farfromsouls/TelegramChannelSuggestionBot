from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import asyncio
import logging

from .handler import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token="TG_TOKEN")
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())