import unittest
from launch_api import make_api_call

class TestAPI(unittest.TestCase):    
    def test_api_default(self):
        '''
        Test the API call default (all launch objects).
        '''
        response = make_api_call()
        self.assertEqual(response[0], 200)
    
    def test_api_upcoming(self):
        '''
        Test the API call for upcoming launches objects.
        '''
        response = make_api_call('upcoming/')
        self.assertEqual(response[0], 200)
    


if __name__ == '__main__':
    unittest.main()