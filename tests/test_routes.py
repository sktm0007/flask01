import unittest
from app.app import app

class TestRoutes(unittest.TestCase):

    # setting up for testing
    def setUp(self):
        # creating a test client from app
        self.client = app.test_client()

    # test for testing invalid request
    def test_route_invalid_method(self):
        # sending post request to a get request homepage
        response = self.client.post('/')
        # checking if the response with the 405 (method not allowed) code
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()