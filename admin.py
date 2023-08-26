import sqlite3

class Admin:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect_to_db()

    def connect_to_db(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close_db_connection(self):
        if self.conn:
            self.conn.close()

    def authenticate(self, username, password):
        self.cursor.execute('SELECT id FROM admin WHERE username = ? AND password = ?', (username, password))
        result = self.cursor.fetchone()
        return result is not None