import sqlite3

with sqlite3.connect("database.db") as connect:
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS password_data
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT,
        username TEXT,
        password TEXT
        )
    ''')
