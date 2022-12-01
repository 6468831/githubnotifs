import json
import requests

URL = 'https://a9d3-87-255-31-80.eu.ngrok.io'

HEADERS = {
    'Content-Type': 'application/json'
}

DATA = {
    'foo': 'bar'
}

r = requests.post(URL, headers=HEADERS, data=json.dumps(DATA))
print(r)