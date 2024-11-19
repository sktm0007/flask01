import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class TestDatabaseWrite(unittest.TestCase):
    """Test the database write operation."""

    def setUp(self):
        """Set up the MongoDB client."""
        self.client = MongoClient(
            f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@shop.cqyex.mongodb.net/?retryWrites=true&w=majority&appName=shop"
        )
        self.db = self.client.app  # Use the correct database
        self.products_collection = self.db.products  # Use the correct collection

    def test_write_data_to_db(self):
        """Test inserting a new product into the database."""
        # Prepare the new data to insert
        new_product = {
            "name": "Product 3",
            "image": "/static/images/product3.jpg",
            "price": 9.99,
            "tag": "new"
        }

        # Insert the new product into the collection
        result = self.products_collection.insert_one(new_product)

        # Query the collection to check if the document is inserted
        inserted_product = self.products_collection.find_one({"name": "Product 3"})

        # Assertions
        self.assertIsNotNone(inserted_product)  # Check if the product was inserted
        self.assertEqual(inserted_product["name"], "Product 3")  # Verify the name
        self.assertEqual(inserted_product["price"], 9.99)  # Verify the price

        # Optionally, clean up the test data after the test (delete the inserted product)
        self.products_collection.delete_one({"name": "Product 3"})

if __name__ == "__main__":
    unittest.main()
