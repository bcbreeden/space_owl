import unittest
from api.api import make_api_call, _get_api_base

class TestAPI(unittest.TestCase):
    def test_dev_api_stub(self):
        '''
        Test the function that builds the API stub (dev).
        '''
        test_base = _get_api_base(dev=True)
        self.assertEqual(test_base, 'https://lldev.thespacedevs.com/2.2.0/')

    def test_prod_api_stub(self):
        '''
        Test the function that builds the API stub (prod).
        '''
        prod_base = _get_api_base(dev=False)
        self.assertEqual(prod_base, 'https://ll.thespacedevs.com/2.2.0/')

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
        response = make_api_call('launch/upcoming', dev=True)
        self.assertEqual(response[0], 200)
    
    def test_api_failure(self):
        '''
        Test the API call when the endpoint does not exist.
        '''
        response = make_api_call('hooplah', dev=True)
        self.assertEqual(response[0], 404)
        self.assertEqual(response[1], None)
    


if __name__ == '__main__':
    unittest.main()