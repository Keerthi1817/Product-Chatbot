"""from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load your dataset once when the server starts
df = pd.read_csv("grocery_products_500.csv")
product_names_lower = df['product_name'].str.lower().tolist()


def search_products(input_text):
    input_text = input_text.lower()
    for index, product_name in enumerate(product_names_lower):
        if input_text in product_name:
            return [df.iloc[index]]
    return []


def format_response(matches):
    if len(matches) == 0:
        return "Sorry, I couldn't find that product."
    row = matches[0]
    name = row['product_name']
    location = row['product_location']
    description = row['product_description']
    stock = row['current_stock']
    response = (
        f"The {name} is located on {location}. "
        f"{description} "
    )
    if stock < 10:
        response += f"Currently, only {stock} units are left. Hurry!"
    else:
        response += f"Available stock: {stock} units."
    return response


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    user_input = data.get('query', '')
    matches = search_products(user_input)
    reply = format_response(matches)
    return jsonify({'reply': reply})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
"""
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
"""from flask import Flask, request, jsonify, send_from_directory


import os

app = Flask(__name__, static_folder='')  # Set static folder if needed

# Load your dataset
df = pd.read_csv("grocery_products_500.csv")
product_names_lower = df['product_name'].str.lower().tolist()


def search_products(input_text):
    input_text = input_text.lower()
    for index, product_name in enumerate(product_names_lower):
        if input_text in product_name:
            return [df.iloc[index]]
    return []


def format_response(matches):
    if len(matches) == 0:
        return "Sorry, I couldn't find that product."
    row = matches[0]
    name = row['product_name']
    location = row['product_location']
    description = row['product_description']
    stock = row['current_stock']
    response = (
        f"The {name} is located on {location}. "
        f"{description} "
    )
    if stock < 10:
        response += f"Currently, only {stock} units are left. Hurry!"
    else:
        response += f"Available stock: {stock} units."
    return response


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    user_input = data.get('query', '')
    matches = search_products(user_input)
    reply = format_response(matches)
    return jsonify({'reply': reply})

# Serve the index.html directly when root is accessed


@app.route('/')
def index():
    # Assumes index.html is in same folder
    return send_from_directory('', 'index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # run your Flask app on port 5000"""

app = Flask(__name__)  # Initialize Flask app
CORS(app)  # Enable CORS

# Load your dataset
df = pd.read_csv("grocery_products_500.csv")
product_names_lower = df['product_name'].str.lower().tolist()


def search_products(input_text):
    input_text = input_text.lower()
    for index, product_name in enumerate(product_names_lower):
        if input_text in product_name:
            return [df.iloc[index]]
    return []


def format_response(matches):
    if len(matches) == 0:
        return "Sorry, I couldn't find that product."
    row = matches[0]
    name = row['product_name']
    location = row['product_location']
    description = row['product_description']
    stock = row['current_stock']
    response = (
        f"The {name} is located on {location}. "
        f"{description} "
    )
    if stock < 10:
        response += f"Currently, only {stock} units are left. Hurry!"
    else:
        response += f"Available stock: {stock} units."
    return response


@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({'reply': "No query provided."})

        user_input = data['query']
        print(f"Received query: {user_input}")
        matches = search_products(user_input)
        reply = format_response(matches)
        return jsonify({'reply': reply})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'reply': "There was an error processing your request."})


@app.route('/')
def index():
    # Assumes index.html is in the same directory as this script
    return send_from_directory('', 'index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Run the Flask app
