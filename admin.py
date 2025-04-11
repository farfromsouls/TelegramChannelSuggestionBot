from data import *


async def check_bd():
    id = await get_a_user() # айдишник первого типа в базе который is_asking
    return id
    

async def FirstTipochek(id):
    text = await Announc(get_brand(id), get_name(id), get_overview(id), get_price(id), toAdmin=True)
    photo_file = await get_photo(id)
    return [text, photo_file]