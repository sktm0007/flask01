import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class TestDatabaseRead(unittest.TestCase):
    """Test the database read operation."""

    def setUp(self):
        """Set up the MongoDB client."""
        self.client = MongoClient(
            f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@shop.cqyex.mongodb.net/?retryWrites=true&w=majority&appName=shop"
        )

    def test_ping_database(self):
        """Test the connection to the database by pinging it."""
        response = self.client.admin.command("ping")  # Perform the ping
        self.assertEqual(response["ok"], 1.0)  # Assert the ping was successful

if __name__ == "__main__":
    unittest.main()
