import sqlite3

# Соединение с базой данных (если базы нет, она будет создана)
conn = sqlite3.connect('database.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы "about"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS about (
        id INTEGER PRIMARY KEY,
        our_service TEXT,
        what_do_i_pay TEXT,
        our_service_prices TEXT,
        payment_in_rubles TEXT,
        payment_in_yuan TEXT,
        blank TEXT,
        default_package TEXT,
        cardboard_corners_package TEXT,
        wood_pacage TEXT,
        self_ransom TEXT,
        scheme_of_work TEXT,
        connect_with_us TEXT
    )
''')

# Создание таблицы "picture"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS picture (
        id INTEGER PRIMARY KEY,
        pictires BLOB
    )
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных и таблицы успешно созданы.")
