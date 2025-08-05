import pprint
import requests

url = 'http://5.63.153.31:5051/v1/account'

headers = {
'accept': '*/*',
'Content-Type': 'application/json'
}

json = {
  "login": "reyner_test",
  "email": "reyner_test@mail.ru",
  "password": "123456789"
}

response = requests.post(
    url=url,
    headers=headers,
    json=json
)

print(response.status_code)
pprint.pprint(response.json())

headers = {
    'accept': 'text/plain',}

response = requests.put('http://5.63.153.31:5051/v1/account/a74fbca7-ccf0-4dbd-82a4-a7eaaa13f466', headers=headers)

print(response.status_code)
pprint.pprint(response.json())


