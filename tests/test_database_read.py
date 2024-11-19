import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class TestDatabaseRead(unittest.TestCase):

    def setUp(self):
        # creating an instance to connect to MongoDB
        self.client = MongoClient(
            # retrieving data from env file to use for db
            f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@shop.cqyex.mongodb.net/?retryWrites=true&w=majority&appName=shop"
        )

    # checking for ping
    def test_ping_database(self):
        # performing the ping
        response = self.client.admin.command("ping")
        # checking if the ping was successfull
        self.assertEqual(response["ok"], 1.0)

if __name__ == "__main__":
    unittest.main()
