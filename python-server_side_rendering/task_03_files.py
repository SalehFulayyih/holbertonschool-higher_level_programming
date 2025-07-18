"""
Flask App - Task 3: Display Products from JSON or CSV

This app reads product data from either a JSON or CSV file, based on
a query parameter 'source'. It optionally filters by product 'id'.
Results are rendered to a Jinja template.

Author: Your Name
Date: 2025-07
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_products(filepath):
    """
    Reads product data from a JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        list of dict: List of product dictionaries.
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []


def read_csv_products(filepath):
    """
    Reads product data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        list of dict: List of product dictionaries.
    """
    products = []
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert price and id to appropriate types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products


@app.route('/products')
def products():
    """
    Route handler for /products.

    Reads product data from JSON or CSV based on query param 'source'.
    Optionally filters the products by 'id'.
    Displays an error if the source is invalid or the ID is not found.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    # Validate source and read data
    if source == 'json':
        products = read_json_products('products.json')
    elif source == 'csv':
        products = read_csv_products('products.csv')
    else:
        error = "Wrong source. Please use ?source=json or ?source=csv."

    # Filter by ID if provided and data was loaded successfully
    if product_id and not error:
        try:
            product_id = int(product_id)
            product = next((p for p in products if p['id'] == product_id), None)
            if product:
                products = [product]
            else:
                error = f"Product with ID {product_id} not found."
                products = []
        except ValueError:
            error = "Invalid ID format. ID must be an integer."
            products = []

    return render_template('product_display.html', products=products, error=error)


if __name__ == '__main__':
    # Run the app on host=0.0.0.0 for compatibility with sandbox environments
    app.run(debug=True, host='0.0.0.0', port=5000)
