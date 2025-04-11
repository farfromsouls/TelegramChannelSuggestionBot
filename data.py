import sqlite3
from aiogram.types import FSInputFile
from buttons import testbtn

# connecting to db
db_path = 'db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
last_command TEXT,
is_asking INTEGER,
name TEXT,
brand TEXT,
price INTEGER,
description TEXT,
photo TEXT,
last_message TEXT)''')


async def check_id(id):
    cursor.execute('SELECT id FROM Users WHERE id = ?', (id,))
    try:
        id = cursor.fetchone()[0]
    except:
        return 0


async def set_id(id):
    cursor.execute('INSERT INTO Users (id) VALUES(?)', (id,))
    conn.commit()


async def delete_user(id):
    cursor.execute('DELETE FROM Users WHERE id = ?', (id,))
    conn.commit()


async def get_lm(id):
    cursor.execute('SELECT last_command FROM Users WHERE id = ?', (id,))
    lm = cursor.fetchone()[0]
    return lm


async def set_lm(id, text):
    cursor.execute('UPDATE Users SET last_command = ? WHERE id = ?', (text, id))
    conn.commit()


async def set_ia(id, val):
    cursor.execute('UPDATE Users SET is_asking = ? WHERE id = ?', (val, id))
    conn.commit()


async def get_ia(id):
    cursor.execute('SELECT is_asking FROM Users WHERE id = ?', (id,))
    ia = cursor.fetchone()[0]
    return ia


async def get_alen_users():
    cursor.execute('SELECT id FROM Users WHERE is_asking = ?', (1,))
    if cursor.fetchone() == None:
        return 0
    a_users = len(cursor.fetchone())
    return a_users


async def set_lastchm(id, text):
    cursor.execute('UPDATE Users SET last_message = ? WHERE id = ?', (text, id))
    conn.commit()


async def set_brand(id, text):
    cursor.execute('UPDATE Users SET brand = ? WHERE id = ?', (text, id))
    conn.commit()


async def set_name(id, text):
    cursor.execute('UPDATE Users SET name = ? WHERE id = ?', (text, id))
    conn.commit()


async def set_ove(id, text):
    cursor.execute('UPDATE Users SET description = ? WHERE id = ?', (text, id))
    conn.commit()


async def set_price(id, text):
    cursor.execute('UPDATE Users SET price = ? WHERE id = ?', (text, id))
    conn.commit()

async def get_a_user():
    cursor.execute('SELECT id FROM Users WHERE is_asking = ?', (1,))
    a_user = cursor.fetchone()[0]
    return a_user

def get_brand(id):
    cursor.execute('SELECT brand FROM Users WHERE id = ?', (id,))
    brand = cursor.fetchone()[0]
    return brand


def get_name(id):
    cursor.execute('SELECT name FROM Users WHERE id = ?', (id,))
    name = cursor.fetchone()[0]
    return name


def get_overview(id):
    cursor.execute('SELECT description FROM Users WHERE id = ?', (id,))
    overview = cursor.fetchone()[0]
    return overview


def get_price(id):
    cursor.execute('SELECT price FROM Users WHERE id = ?', (id,))
    price = cursor.fetchone()[0]
    return price


async def set_photo(id, link):
    cursor.execute('UPDATE Users SET photo = ? WHERE id = ?', (link, id))
    conn.commit()


async def get_photo(id):
    cursor.execute('SELECT photo FROM Users WHERE id = ?', (id,))
    photo = cursor.fetchone()[0]
    return photo

async def get_lastchm(id):
    cursor.execute('SELECT last_message FROM Users WHERE id = ?', (id,))
    lastchm = cursor.fetchone()[0]
    return lastchm


async def Announc(brend, name, overview, price, toAdmin=False):
    global textmess
    textmess = (f'Бренд: {brend} \n'
                 f'Название: {name} \n'
                 f'Описание: {overview} \n'
                 f'Цена: {price} \n\n\n')
    if toAdmin == False:
        textmess = textmess + f'Хотите внести изменения? \n'
    return textmess

async def changes(id, text, message):   
    lastchm = await get_lastchm(id)
    
    if lastchm == "Бренд":
        await set_brand(id, text)
    elif lastchm == "Название":
        await set_name(id, text)  
    elif lastchm == "Описание":
        await set_ove(id, text) 
    elif lastchm == "Цена":
        await set_price(id, text)
    
    if lastchm in ["Бренд", "Название", "Описание", "Цена"]:
        photo_file = FSInputFile(await get_photo(id))
        text = await Announc(get_brand(id), get_name(id), get_overview(id), get_price(id))
        await message.answer_photo(photo=photo_file, reply_markup=testbtn, caption=text)
            