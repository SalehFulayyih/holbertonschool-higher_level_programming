import sqlite3
import os


def create_database():
    db_path = 'products.db'

    # Delete existing database file if it exists (and might be corrupted)
    if os.path.exists(db_path):
        os.remove(db_path)

    # Now create a fresh database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    cursor.executemany('''
        INSERT INTO Products (id, name, category, price)
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ])

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
