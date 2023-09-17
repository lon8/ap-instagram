import json
import requests

headers = {
	"X-RapidAPI-Key": "618a643552msh68bf479e095e0aep1eca05jsnf3bb7b685754",
	"X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
}

json_data = {
    'search_query': 'kostyukkova',
    'user_id': 52,
}

# url = "https://instagram-scraper-20231.p.rapidapi.com/userfollowing/25025320/100/%7Bend_cursor%7D"

req = requests.post('http://127.0.0.1:5000/', json=json_data)

print(req.text)
