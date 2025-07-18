from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data(filepath):
    """
    Reads product data from a JSON file.

    Args:
        filepath (str): Path to JSON file.

    Returns:
        list: List of products as dictionaries.
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv_data(filepath):
    """
    Reads product data from a CSV file.

    Args:
        filepath (str): Path to CSV file.

    Returns:
        list: List of products as dictionaries.
    """
    products = []
    try:
        with open(filepath, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    products.append({
                        'id': int(row['id']),
                        'name': row['name'],
                        'category': row['category'],
                        'price': float(row['price'])
                    })
                except (ValueError, KeyError):
                    continue
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

def read_sql_data(db_path):
    """
    Reads product data from a SQLite database.

    Args:
        db_path (str): Path to the SQLite database.

    Returns:
        list: List of products as dictionaries.
    """
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except Exception as e:
        print(f"Error reading SQLite DB: {e}")
    return products

@app.route('/products')
def products():
    """
    Route to display products from JSON, CSV, or SQLite source.
    Accepts:
        - source: 'json', 'csv', or 'sql'
        - id: optional product ID to filter
    """
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products = []

    # Choose source
    if source == 'json':
        products = read_json_data('products.json')
    elif source == 'csv':
        products = read_csv_data('products.csv')
    elif source == 'sql':
        products = read_sql_data('products.db')
    else:
        error = "Wrong source"

    # Filter by ID if provided
    if product_id and not error:
        try:
            product_id = int(product_id)
            product = next((p for p in products if p['id'] == product_id), None)
            if product:
                products = [product]
            else:
                error = "Product not found"
                products = []
        except ValueError:
            error = "Invalid ID format. ID must be an integer."
            products = []

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
