import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def create_table():
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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

def get_car(car_id):
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM inventory WHERE id = ?', (car_id,))
    car = cursor.fetchone()
    connect.close()
    return car

def edit_car(car_id, make, model, reg, mileage, year, price, colour):
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('''
        UPDATE inventory
        SET MAKE = ?, MODEL = ?, REG = ?, MILEAGE = ?, YEAR = ?, PRICE = ?, COLOUR = ?
        WHERE id = ?
    ''', (make, model, reg, mileage, year, price, colour, car_id))
    connect.commit()
    connect.close()

def remove_car(car_id):
    connect = sqlite3.connect('inventory.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM inventory WHERE id = ?', (car_id,))
    connect.commit()
    connect.close()

@app.route('/catalogue', methods=['GET'])
def catalogue():
    cars = get_all_cars()
    return render_template('catalogue.html', cars=cars)

@app.route('/edit/<int:car_id>', methods=['GET', 'POST'])
def edit(car_id):
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        reg = request.form['reg']
        mileage = request.form['mileage']
        year = request.form['year']
        price = request.form['price']
        colour = request.form['colour']
        edit_car(car_id, make, model, reg, mileage, year, price, colour)
        return redirect(url_for('catalogue'))
    
    car = get_car(car_id)
    return render_template('edit.html', car=car)

@app.route('/remove/<int:car_id>', methods=['POST'])
def remove(car_id):
    remove_car(car_id)
    return redirect(url_for('catalogue'))

if __name__ == '__main__':
    create_table()  # Ensure the table exists
    app.run(debug=True)