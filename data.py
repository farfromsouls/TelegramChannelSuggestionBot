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
photo TEXT)''')


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
