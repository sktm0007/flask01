import os
from pymongo import MongoClient
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# assignment 3
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

# Print debug information
print(f"Initializing Flask app with MongoDB credentials: {MONGODB_USERNAME}, {MONGODB_PASSWORD}")


# Connection to database

# assignment 2
# client = MongoClient(f"mongodb+srv://admin:admin@shop.cqyex.mongodb.net/?retryWrites=true&w=majority&appName=shop")

# assignment 3
client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@shop.cqyex.mongodb.net/?retryWrites=true&w=majority&appName=shop")

db = client.app
products_collection = db.products


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products')
def products():
    products = list(products_collection.find())
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
