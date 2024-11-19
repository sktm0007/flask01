import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class TestDatabaseWrite(unittest.TestCase):

    def setUp(self):
        # creating an instance to connect to MongoDB
        self.client = MongoClient(
            f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@shop.cqyex.mongodb.net/?retryWrites=true&w=majority&appName=shop"
        )
        # accessing the database
        self.db = self.client.app
        # accessing product collection
        self.products_collection = self.db.products

    # inserting new data to the database
    def test_write_data_to_db(self):
        new_product = {
            "name": "Product 3",
            "image": "/static/images/product3.jpg",
            "price": 9.99,
            "tag": "new"
        }

        # adding new product
        result = self.products_collection.insert_one(new_product)

        # finding the product
        inserted_product = self.products_collection.find_one({"name": "Product 3"})
        # checking if the product was added
        self.assertIsNotNone(inserted_product)
        # checking the name of new product in database
        self.assertEqual(inserted_product["name"], "Product 3")

if __name__ == "__main__":
    unittest.main()
