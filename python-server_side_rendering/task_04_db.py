#!/usr/bin/env python3
""" Flask app to display product data from JSON, CSV, or SQLite """

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)
DB_FILE = 'my_products.db'  # Updated name


def read_json():
    try:
        with open('products.json') as file:
            return json.load(file).get('items', [])
    except Exception:
        return []


def read_csv():
    try:
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception:
        return []


def read_sql(product_id=None):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        if product_id:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except sqlite3.Error:
        return []


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql(product_id)
    else:
        error = "Wrong source"

    if product_id and source != 'sql':
        products = [p for p in products if str(p.get('id')) == str(product_id)]

    if not products and not error:
        error = "Product not found"

    return render_template('product_display.html', products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
