import json
import requests

headers = {
	"X-RapidAPI-Key": "618a643552msh68bf479e095e0aep1eca05jsnf3bb7b685754",
	"X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
}

json_data = {
    'search_query': 'vladkanatov',
    'user_id': 52,
}

req = requests.post('http://127.0.0.1:8080/', json=json_data)
# req = requests.post('http://127.0.0.1:8080/', json=json_data)

print(req.text)
