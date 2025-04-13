from data import *


async def check_bd():
    id = await get_a_user() # айдишник первого типа в базе который is_asking
    return id
    

async def FirstTipochek(id):
    photo_file = FSInputFile(await get_photo(id))
    brand = await get_brand(id)
    name = await get_name(id)
    overview = await get_overview(id)
    price = await get_brand(id)

    text = await Announc(brand, name, overview, price)
    photo_file = await get_photo(id)
    return [text, photo_file]