import requests

def make_api_call(endpoint=''):
    '''
    Makes an api call to Launch Library 2. If not endpoint is provided, a call is made to the stub by default.
    '''
    api_url = '{}{}'.format(_get_api_stub(), endpoint)
    response = requests.get(api_url)
    json = response.json()
    status_code = response.status_code
    return[status_code, json]

def _get_api_stub(dev=True):
    '''
    Builds the API stub. Defaults to the development instance of the API.
    '''
    stub = 'https://lldev.thespacedevs.com/2.2.0/launch/'
    if not dev:
        stub = 'https://ll.thespacedevs.com/2.2.0/launch/'
    return stub
