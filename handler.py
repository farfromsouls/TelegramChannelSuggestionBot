from aiogram import types

from .main import dp
from .buttons import *


@dp.message()
async def handler(message: types.Message):

    id = message.from_user.id
    text = message.text