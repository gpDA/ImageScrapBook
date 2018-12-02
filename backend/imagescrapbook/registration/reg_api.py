import json
import requests
import os

AUTH_ENDPOINT = 'http://127.0.0.1:8000/api-token-create/'
REFRESH_ENDPOINT = 'http://127.0.0.1:8000/api-token-refresh/'
ENDPOINT = 'http://127.0.0.1:8000/'
headers = {
    "Content-Type": "application/json"
}

data = {
    'username': 'geonpyung22',
    'password': 'qazwsx12'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print(token)

refresh_data = {
    'token': token
}

new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
new_token = new_response.json()#['token']

print(new_token)