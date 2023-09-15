import json
import requests

json_data = {
    'search_query': 'vladkanatov',
    'user_id': 1,
}

req = requests.post('http://127.0.0.1:8000/', json=json_data)

print(req.text)
