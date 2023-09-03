import json
import requests

data = {
    'username': 'vladkanatov'
}

req = requests.post('http://127.0.0.1:8000/userInfo', json=data)

print(req.text)

### USERPOSTS

# url = "https://instagram-scraper-20231.p.rapidapi.com/userposts/16417251805/100/%7Bend_cursor%7D"

# headers = {
# 	"X-RapidAPI-Key": "55453220d9msh8691df94bd03ef9p15447djsn954109d2e534",
# 	"X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# with open('userposts.json', 'w', encoding='utf') as file:
#     json.dump(response.json(), file, indent=4, ensure_ascii=False)

# print('Done')

### USERINFO

# import requests

# url = "https://instagram-scraper-20231.p.rapidapi.com/userinfo/vladkanatov"

# headers = {
# 	"X-RapidAPI-Key": "55453220d9msh8691df94bd03ef9p15447djsn954109d2e534",
# 	"X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# with open('userinfo.json', 'w', encoding='utf-8') as file:
#     json.dump(response.json(), file, indent=4, ensure_ascii=False)

# print('Done')