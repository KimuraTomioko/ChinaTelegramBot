import sqlite3

# Соединение с базой данных (если базы нет, она будет создана)
conn = sqlite3.connect('database.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы "about"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS about (
        id INTEGER PRIMARY KEY,
        our_service TEXT
    )
''')

# Создание таблицы "picture"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS picture (
        id INTEGER PRIMARY KEY,
        photo BLOB
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin (
               id INTEGER PRIMARY KEY,
               username TEXT,
               password TEXT
    )
''')


# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных и таблицы успешно созданы.")
