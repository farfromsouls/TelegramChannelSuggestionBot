import sqlite3
import datetime

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


def check_id(id):
    cursor.execute('SELECT id FROM Users WHERE id = ?', (id,))
    try:
        id = cursor.fetchone()[0]
    except:
        return 0


def set_id(id):
    cursor.execute('INSERT INTO Users (id) VALUES(?)', (id,))
    conn.commit()


def get_lm(id):
    cursor.execute('SELECT last_command FROM Users WHERE id = ?', (id,))
    lm = cursor.fetchone()[0]
    return lm


async def set_lm(id, text):
    cursor.execute('UPDATE Users SET last_command = ? WHERE id = ?', (text, id))
    conn.commit()


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




def set_photo(id, link):
    cursor.execute('UPDATE Users SET photo = ? WHERE id = ?', (link, id))
    conn.commit()


def get_lastchm(id):
    cursor.execute('SELECT last_message FROM Users WHERE id = ?', (id,))
    lastchm = cursor.fetchone()[0]
    return lastchm


def Announc(brend, name, overview, price):
    global textmess
    textmess = (f'Бренд: {brend} \n'
                 f'Название: {name} \n'
                 f'Описание: {overview} \n'
                 f'Цена: {price} \n\n\n'
                 f'Хотите внести изменения? \n')
    return textmess

async def changes(text):   
    if text == "Бренд":
        await bot.send_message(id, "Напиши Бренд ")
        await set_brand(id, "Напиши название ")       
    elif text == "Название":
        await bot.send_message(id, "Напиши название ")
        await set_name(id, "Напиши название ")  
    elif text == "Описание":
        await bot.send_message(id, "Напиши Бренд ")
        await set_ove(id, "Напиши название ")  
    elif text == "Цена":
        await bot.send_message(id, "Напиши Бренд ")
        await set_price(id, "Напиши название ") 
    else:
        print("неправильный ввод")
        return
    Announc(get_brand(id), get_name(id), get_overview(id), get_price(id))