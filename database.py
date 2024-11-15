import sqlite3

connect = sqlite3.connect('inventory.db')

cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        MAKE TEXT,
        MODEL TEXT,
        REG BLOB,
        MILEAGE INTEGER,
        YEAR INTEGER,
        PRICE INTEGER,
        COLOUR TEXT
    )
''');

connect.commit()
connect.close()