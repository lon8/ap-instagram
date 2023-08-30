import requests

data = {
    'Username': 'vladkanatov'
}

req = requests.get('http://127.0.0.1:8000/userInfo', json=data)

print(req.text)