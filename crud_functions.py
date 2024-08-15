import sqlite3

connection = sqlite3.connect('product_data.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT,
    description TEXT,
    price INT
    )
    ''')
    connection.commit()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    )
    ''')
    connection.commit()

initiate_db()

def add_user(username, email, age):
    connection = sqlite3.connect('product_data.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)
    ''', (username, email, age, 1000))
    connection.commit()

def is_included(username):
    connection = sqlite3.connect('product_data.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT id FROM Users WHERE username = ?', (username,)).fetchone()
    if check_user is None:
        connection.commit()
        return False
    else:
        connection.commit()
        return True


def get_all_products():
    connection = sqlite3.connect('product_data.db')
    cursor = connection.cursor()
    products = cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    return products

connection.commit()
connection.close()