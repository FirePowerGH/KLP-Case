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
                    salt VARCHAR(255) NOT NULL,
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

    def regUser(self, navn, password):
        from random import randint
        import hashlib

        salt = str(randint(1, 99))
        salt = hashlib.sha256(salt.encode()).hexdigest()

        password = password + salt
        password = hashlib.sha256(password.encode()).hexdigest()

        num1 = randint(1000, 9999)
        num2 = randint(100, 999)
        kontonr: str = ' '.join(['8317', str(num1), str(num2)])

        with self:
            self.cursor.execute(
                '''INSERT INTO brukere (navn, password, salt, kontonr)
                VALUES (?, ?, ?, ?)''',
                (navn, password, salt, kontonr)
            )
    
    def checkUser(self, navn, password):
        import hashlib

        with self:
            self.cursor.execute(
                '''SELECT password, salt FROM brukere WHERE navn = ?''',
                (navn,)
            )
            res = self.cursor.fetchone()

            if res is None:
                return False

            password = password + res[1]
            password = hashlib.sha256(password.encode()).hexdigest()

            return password == res[0]