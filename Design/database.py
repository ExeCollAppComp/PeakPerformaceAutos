import sqlite3
import csv
def create_table():
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
    ''')
    connect.commit()
    connect.close()

def add_car(make, model, reg, mileage, year, price, colour):
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('''
        INSERT INTO inventory (MAKE, MODEL, REG, MILEAGE, YEAR, PRICE, COLOUR)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (make, model, reg, mileage, year, price, colour))
    connect.commit()
    connect.close()

def get_all_cars():
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM inventory')
    cars = cursor.fetchall()
    connect.close()
    return cars

def update_car(make, model, new_price):
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('''
        UPDATE inventory
        SET PRICE = ?
        WHERE MAKE = ? AND MODEL = ?
    ''', (new_price, make, model))
    connect.commit()
    connect.close()

def delete_car(make, model):
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('''
        DELETE FROM inventory
        WHERE MAKE = ? AND MODEL = ?
    ''', (make, model))
    connect.commit()
    connect.close()

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            make, model, reg, mileage, year, price, colour = row
            add_car(make, model, reg, mileage, year, price, colour)

create_table()

read_csv_file('cars.csv')

cars = get_all_cars()
for car in cars:
    print(car)
