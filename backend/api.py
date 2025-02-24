import sqlite3

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect('backend/database.db')
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            if exc_type is not None:
                self.conn.rollback()
                print(f'An exception of type {exc_type} occurred')
                print(exc_value)
            else:
                self.conn.commit()
            self.conn.close()

    def createTable(self):
        with self:
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS brukere (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    navn VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    kontonr INT NOT NULL
                )'''
            )
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS transaksjon (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    brukerid INTEGER NOT NULL,
                    FOREIGN KEY (brukerid) REFERENCES brukere(id)
                )'''
            )

    def regUser(self, navn, password, kontonr):
        from random import randint

        num1 = randint(1000, 9999)
        num2 = randint(100, 999)
        kontonr: str = ' '.join(['8317', str(num1), str(num2)])
        print(kontonr)

        # with self:
        #     self.cursor.execute(
        #         '''INSERT INTO brukere (navn, password, kontonr)
        #         VALUES (?, ?, ?)''',
        #         (navn, password, kontonr)
        #     )