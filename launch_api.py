import requests

API_STUB = 'https://ll.thespacedevs.com/2.2.0/launch/'

def make_api_call(endpoint=''):
    '''
    Makes an api call to Launch Library 2. If not endpoint is provided, a call is made to the stub by default.
    '''
    api_url = '{}{}'.format(API_STUB, endpoint)
    response = requests.get(api_url)
    json = response.json()
    status_code = response.status_code
    return[status_code, json]