import requests
import logging

def make_api_call(endpoint='', dev=True):
    '''
    Makes an api call to Launch Library 2. If no endpoint is provided, a call is made to the stub by default.

    It is recommended that an endpoint be provided to get some meaningful data returned.

     Docs: https://lldev.thespacedevs.com/docs/
    '''
    api_url = '{}{}'.format(_get_api_base(dev), endpoint)
    response = requests.get(api_url)
    try:
        json = response.json()
    except Exception as e:
        logging.warning('No JSON payload present: {}'.format(api_url))
        logging.warning('Status Code: {}'.format(response.status_code))
        logging.warning('Exception returned: {} - {}'.format(type(e).__name__, e))
        json = None
    status_code = response.status_code
    return[status_code, json]

def _get_api_base(dev):
    '''
    Builds the API url base. Defaults to the development instance of the API.
    '''
    stub = 'https://lldev.thespacedevs.com/2.2.0/'
    if not dev:
        stub = 'https://ll.thespacedevs.com/2.2.0/'
    return stub
