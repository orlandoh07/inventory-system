import sqlite3

def get_connection():
    connection = sqlite3.connect("database/inventory.db")
    return connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            quantity INT,
            category_id INT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    connection.commit()
    connection.close()

# products CRUD
def add_product(name, price, quantity, category_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity, category_id) VALUES (?, ?, ?, ?)", (name, price, quantity, category_id))
    connection.commit()
    connection.close()

def get_all_products():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    connection.close()
    return products
    
def update_product(id, name, price, quantity, category_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET name = ?, price = ?, quantity = ?, category_id = ? WHERE id = ?",
    (name, price, quantity, category_id, id)
    )
    connection.commit()
    connection.close()
    
def delete_product(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    connection.commit()
    connection.close()

# categories CRUD
def add_category(name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    connection.commit()
    connection.close()

def get_all_categories():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    connection.close()
    return categories

def update_category(id, name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE categories SET name = ? WHERE id = ?", (name, id))
    connection.commit()
    connection.close()

def delete_category(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM categories WHERE id = ?", (id,))
    connection.commit()
    connection.close()

# users CRUD
def add_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    connection.commit()
    connection.close()

def get_user_by_username(username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    users = cursor.fetchall()
    connection.close()
    return users

def update_user(id, name, password):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET name = ?, password = ? WHERE id = ?", (name, password, id))
    connection.commit()
    connection.close()

def delete_user(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    connection.commit()
    connection.close()