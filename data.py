import sqlite3
from aiogram.types import FSInputFile
from buttons import userbtn


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
photo TEXT,async 
last_message TEXT,
index_lol INTEGER )''')


async def max_index():
    cursor.execute('SELECT MAX(index_lol) FROM Users ')
    max_ind=cursor.fetchone()[0]
    print(max_ind)
    if max_ind == None:
        return 0
    return max_ind


async def min_index():
    cursor.execute('SELECT MIN(index_lol) FROM Users ')
    min_ind=cursor.fetchone()[0]
    print(min_ind)
    if min_ind == None:
        return 0
    return min_ind


async def check_id(id):
    cursor.execute('SELECT id FROM Users WHERE id = ?', (id,))
    id = cursor.fetchone()
    if id != None:
        return id
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
    spisok=cursor.fetchall()
    
    if spisok == None:
        return 0
    
    a_users = len(spisok)
    return a_users


async def set_lastchm(id, text):
    cursor.execute('UPDATE Users SET last_message = ? WHERE id = ?', (text, id))
    conn.commit()


async def set_brand(id, text):
    cursor.execute('UPDATE Users SET brand = ? WHERE id = ?', (text, id))
    conn.commit()


async def set_ind(id):
    cursor.execute('UPDATE Users SET index_lol = ? WHERE id = ?',( await max_index() + 1, id))
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
    min_tip = await min_index()
    cursor.execute('SELECT id FROM Users WHERE index_lol = ? ', (min_tip,))
    tip = cursor.fetchone()[0] 
    return tip
    

async def get_brand(id):
    cursor.execute('SELECT brand FROM Users WHERE id = ?', (id,))
    brand = cursor.fetchone()[0]
    return brand


async def get_ind(id):
    cursor.execute('SELECT index_lol FROM Users WHERE id = ?', (id,))
    indll = cursor.fetchone()[0]
    return indll


async def get_name(id):
    cursor.execute('SELECT name FROM Users WHERE id = ?', (id,))
    name = cursor.fetchone()[0]
    return name


async def get_overview(id):
    cursor.execute('SELECT description FROM Users WHERE id = ?', (id,))
    overview = cursor.fetchone()[0]
    return overview


async def get_price(id):
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
                 f'Цена: {price} \n')
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
        brand = await get_brand(id)
        name = await get_name(id)
        overview = await get_overview(id)
        price = await get_price(id)
        
        text = await Announc(brand, name, overview, price)
        await message.answer_photo(photo=photo_file, reply_markup=userbtn, caption=text)