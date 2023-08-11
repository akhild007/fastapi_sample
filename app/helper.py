import requests
from decouple import config

def make_get_request(url, params):
    headers = get_headers()
    data = requests.get(url=url, headers=headers, params=params)
    return data.json()

def make_post_request(url, payload):
    pass


def get_headers():
    return {
        'x-api-key': config('API_KEY')
    }