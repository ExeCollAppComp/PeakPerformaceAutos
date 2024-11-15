import sqlite3

def create_table():
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            MAKE TEXT,
            MODEL TEXT,
            REG TEXT,
            MILEAGE INTEGER,
            YEAR INTEGER,
            PRICE INTEGER,
            COLOUR TEXT
        )
    ''')
    connect.commit()
    connect.close()

def add_car(make, model, reg, mileage, year, price, colour):
    try:
        connect = sqlite3.connect('inventory.db')
        cursor = connect.cursor()
        cursor.execute('''
            INSERT INTO inventory (MAKE, MODEL, REG, MILEAGE, YEAR, PRICE, COLOUR)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (make, model, reg, mileage, year, price, colour))
        connect.commit()
    except sqlite3.DatabaseError as e:
        print(f"Error inserting car: {e}")
    finally:
        connect.close()

def get_all_cars():
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM inventory')
    cars = cursor.fetchall()
    connect.close()
    return cars

def get_car(car_id):
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM inventory WHERE id = ?', (car_id,))
    car = cursor.fetchone()
    connect.close()
    return car

def edit_car(car_id, make, model, reg, mileage, year, price, colour):
    try:
        connect = sqlite3.connect('inventory.db')
        cursor = connect.cursor()
        cursor.execute('''
            UPDATE inventory
            SET MAKE = ?, MODEL = ?, REG = ?, MILEAGE = ?, YEAR = ?, PRICE = ?, COLOUR = ?
            WHERE id = ?
        ''', (make, model, reg, mileage, year, price, colour, car_id))
        connect.commit()
    except sqlite3.DatabaseError as e:
        print(f"Error updating car: {e}")
    finally:
        connect.close()

def remove_car(car_id):
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM inventory WHERE id = ?', (car_id,))
    connect.commit()
    connect.close()
