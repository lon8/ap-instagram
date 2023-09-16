import json
import requests

json_data = {
    'search_query': 'vladkanatov',
    'user_id': 52,
}

req = requests.post('http://127.0.0.1:8080/', json=json_data)

print(req.text)
