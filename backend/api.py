import sqlite3

def createTable():
    # Koble til databasen, eller lage en hvis den ikke finnes
    con = sqlite3.connect('backend/database.db')

    # Lage en cursor for å utføre SQL-spørringer
    cursor = con.cursor()

    # Lage en tabell for bruker informasjon
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS brukere (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            navn VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            tlf INT NOT NULL,
            password VARCHAR(255) NOT NULL,
            fødselnummer INT NOT NULL,
            kontonr INT NOT NULL
        )'''
    )

    # Lage en tabell for transaksjoner
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS transaksjon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brukerid VARCHAR(255) NOT NULL
        )'''
    )

    con.commit()
    cursor.close()
    con.close()