import requests

headers = {
        "X-RapidAPI-Key": "55453220d9msh8691df94bd03ef9p15447djsn954109d2e534",
        "X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
    }


async def user_data_posts(uid : int, is_first : bool) -> dict:
    # Здесь нужно реализовать:
    # Суммарное количество постов на странице
    # Суммарное количество просмотров постов на странице
    # Суммарное количество лайков
    # Суммарное количество репостов
    # Суммарное количество комментариев
    
    # А также:
    # Данные в массиве о каждом посте:
        # Ссылка на пост
        # Ссылка на изображение поста (если есть)
        # Дата поста
        # Количество лайков
        # Количество комментариев
        # Количество просмотров
        # Массив данных с реакциями на пост (лайки, комментарии)


    url = f"https://instagram-scraper-20231.p.rapidapi.com/userposts/{uid}/1000/%7Bend_cursor%7D"

    response = requests.get(url, headers=headers)

    data : dict = response.json()['data']

    total_views_count : int = 0 # Здесь вписываются все просмотры (видеороликов и Reels)
    total_likes_count : int = 0 # Здесь вписываются лайки

    for edge in data['edges']:
        post = edge['node']

        photos = []

        video : bool = post['is_video']

        if video:
            total_views_count += post['video_view_count']
        else:
            try:
                for photos_edge in post['edge_sidecar_to_children']['edges']:
                    photo = photos_edge['node']
                    photos.append(photo['display_url'])
            except:
                photos.append(post['display_url'])



    return

async def user_data_main(username : str) -> dict:
    
    url = f"https://instagram-scraper-20231.p.rapidapi.com/userinfo/{username}"
    
    response = requests.get(url, headers=headers)

    data : dict = response.json()['data']

    main_data = {}

    main_data['profile_link'] = f'https://instagram.com/{username}'
    main_data['username'] = username
    main_data['full_name'] = data['full_name']
    main_data['followers_count'] = data['edge_followed_by']['count']
    main_data['follows_count'] = data['edge_follow']['count']
    main_data['profile_picture'] = data['profile_pic_url_hd']
    main_data['posts_count'] = sum(data["edge_felix_video_timeline"]['count'], data["edge_owner_to_timeline_media"]['count'])

    

def kernel(username : str):
    
    url = f"https://instagram-scraper-20231.p.rapidapi.com/userinfo/{username}"
    
    response = requests.get(url, headers=headers)

    data = response.json()

