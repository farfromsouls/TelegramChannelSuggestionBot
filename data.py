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
description TEXT,
photo TEXT)''')

