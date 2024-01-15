import unittest
from launch_api import make_api_call, _get_api_stub

class TestAPI(unittest.TestCase):
    def test_dev_api_stub(self):
        '''
        Test the function that builds the API stub (dev).
        '''
        test_stub = _get_api_stub(dev=True)
        self.assertEqual(test_stub, 'https://lldev.thespacedevs.com/2.2.0/launch/')

    def test_prod_api_stub(self):
        '''
        Test the function that builds the API stub (prod).
        '''
        prod_stub = _get_api_stub(dev=False)
        self.assertEqual(prod_stub, 'https://ll.thespacedevs.com/2.2.0/launch/')

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