import datetime
import threading
import requests

headers = {
	"X-RapidAPI-Key": "dac62b5a32mshffd641aeed22e7bp16a5bcjsnbd497ab8d5b7",
	"X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
}

def post_likes(shortcode : str):
    
    url = f"https://instagram-scraper-20231.p.rapidapi.com/postlikes/{shortcode}/50/%7Bend_cursor%7D"
    
    response = requests.get(url, headers=headers)
    
    result = []
    
    try:
        data = response.json()['data']
    except:
        return result
    
    for likes in data['likes']:
        like = likes['node']
        
        main_data = {}
        
        main_data['username'] = like['username']
        main_data['profile_pic'] = like['profile_pic_url']
        main_data['profile_url'] = f'https://instagram.com/{like["username"]}'
        main_data['id'] = like["id"]
        
        result.append(main_data)
        
    return result

def post_comments(shortcode : str):
    
    url = f"https://instagram-scraper-20231.p.rapidapi.com/postcomments/{shortcode}/%7Bend_cursor%7D/%7Bscraperid%7D"
    
    result = []

    response = requests.get(url, headers=headers)
    try:    
        data = response.json()['data']
    except:
    	return result
    
    for comment in data['comments']:
        main_data = {}
        
        date = datetime.datetime.fromtimestamp(comment['created_at_utc'])
        
        main_data['date'] = str(date)
        main_data['has_liked_comment'] = comment['has_liked_comment']
        main_data['text'] = comment['text']
        main_data['username'] = comment['user']['username']
        main_data['profile_pic'] = comment['user']['profile_pic_url']
        main_data['profile_url'] = f'https://instagram.com/{comment["user"]["username"]}'
        main_data['id'] = comment["user_id"]
        
        result.append(main_data)
        
    return result
    
def run_multiple_threads(target_function, items):
    # Создайте список потоков
    threads = []

    # Задайте количество потоков, которые вы хотите использовать
    num_threads = 5

    # Создайте и запустите каждый поток
    for item in items:
        thread = threading.Thread(target=target_function, args=(item,))
        thread.start()
        threads.append(thread)

    # Дождитесь завершения всех потоков
    for thread in threads:
        thread.join()

def user_data_followers(uid : int, full_list : list, offset : int = 0, counter : int = 0):
    
    url = f"https://instagram-scraper-20231.p.rapidapi.com/userfollowers/{uid}/100/{offset}"
    
    response = requests.get(url, headers=headers)
    
    data : dict = response.json()['data']
    
    
    
    for user in data['user']:
        main_data = {}
        main_data['username'] = user['username']
        main_data['profile_pic'] = user['profile_pic_url']
        main_data['profile_url'] = f'https://instagram.com/{user["username"]}'
        
        full_list.append(main_data)
    
    if counter != 10:
        try:
            end_cursor = data['end_cursor']
            counter += 1
            user_data_followers(uid=uid, offset=end_cursor, full_list=full_list, counter=counter)
        except:
            return
    else: return

def user_data_following(uid : int, full_list : list, offset : int = 0, counter : int = 0):
    
    url = f"https://instagram-scraper-20231.p.rapidapi.com/userfollowing/{uid}/100/{offset}"

    headers = {
        "X-RapidAPI-Key": "55453220d9msh8691df94bd03ef9p15447djsn954109d2e534",
        "X-RapidAPI-Host": "instagram-scraper-20231.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    
    data : dict = response.json()['data']
    
    for user in data['user']:
        main_data = {}
        main_data['username'] = user['username']
        main_data['profile_pic'] = user['profile_pic_url']
        main_data['profile_url'] = f'https://instagram.com/{user["username"]}'
    
        full_list.append(main_data)
    
    if counter != 10:
        try:
            end_cursor = data['end_cursor']
            counter += 1
            user_data_following(uid=uid, offset=end_cursor, full_list=full_list, counter=counter)
        except:
            return
    else: return

def user_data_posts(uid : int,
                          full_list : list,
                          end_cursor : str = '%7Bend_cursor%7D',
                          counter : int = 0,
                          total_views_count : int = 0,
                          total_likes_count : int = 0,
                          total_posts_count : int = 0,
                          total_comments_count : int = 0) -> int:
    
    url = f"https://instagram-scraper-20231.p.rapidapi.com/userposts/{uid}/1000/{end_cursor}" #%7Bend_cursor%7D

    response = requests.get(url, headers=headers)

    data : dict = response.json()['data']

    total_posts_count += len(data['edges'])

    for edge in data['edges']:
        post = edge['node']
        
        main_data = {}
        
        shortcode = post["shortcode"]
        
        post_like : list = post_likes(shortcode)
        post_comment : list = post_comments(shortcode)
        main_data['likes'] = post_like
        main_data['comments'] = post_comment
        
        main_data['post_url'] = f"https://instagram.com/p/{post['shortcode']}"

        # Дата

        date = post["taken_at_timestamp"]

        post_date = datetime.datetime.fromtimestamp(date)

        main_data['post_date'] = str(post_date)

        # Видео

        video : bool = post['is_video']

        if video:

            view_count = post['video_view_count']

            main_data['view_count'] = view_count

            total_views_count += view_count

        # Фото
        
        photos = []

        try:
            for photos_edge in post['edge_sidecar_to_children']['edges']:
                photo = photos_edge['node']
                photos.append(photo['display_url'])
        except:
            photos.append(post['display_url'])

        main_data['media'] = photos

        # Лайки

        likes_count = post['edge_media_preview_like']['count']

        main_data['likes_count'] = likes_count

        total_likes_count += likes_count

        # Комментарии

        comments_count = post["edge_media_to_comment"]["count"]

        main_data['comments_count'] = comments_count

        total_comments_count += comments_count

        full_list.append(main_data)

    next_page : bool = data['next_page']

    if next_page:
        end = data["end_cursor"]
        counter += 1
        user_data_posts(uid=uid,
                        full_list=full_list,
                        end_cursor=end,
                        counter=counter,
                        total_comments_count=total_comments_count,
                        total_posts_count=total_posts_count,
                        total_views_count=total_views_count)
    elif counter == 10:
          # Здесь очень некорректно сделал, но времени на то, чтобы это переделать нет, потому что надо
          # переписывать очень много кода. По названиям переменных прочитайте, что к чему присвоитс япри
          # окончании работы функции
        return total_posts_count, total_likes_count, total_comments_count, total_views_count
    else: 
        return total_posts_count, total_likes_count, total_comments_count, total_views_count

def user_data_main(username : str) -> dict:
    
    url = f"https://instagram-scraper-20231.p.rapidapi.com/userinfo/{username}"
    
    response = requests.get(url, headers=headers)

    data : dict = response.json()['data']

    main_data = {}

    main_data['id'] = data['id']
    main_data['profile_link'] = f'https://instagram.com/{username}'
    main_data['username'] = username
    main_data['full_name'] = data['full_name']
    main_data['followers_count'] = data['edge_followed_by']['count']
    main_data['follows_count'] = data['edge_follow']['count']
    main_data['avatar_link'] = data['profile_pic_url_hd']
    
    return main_data

    

def kernel(username : str) -> dict:

    result = user_data_main(username=username)

    uid = result['id']

    followers_list = []
    following_list = []
    posts_list = []

    data = {}
    
    total_posts_count, total_likes_count, total_comments_count, total_views_count = user_data_posts(uid, posts_list)
    user_data_followers(uid, followers_list)
    user_data_following(uid, following_list)

    data['total_posts'] = total_posts_count
    data['total_comments'] = total_comments_count
    data['total_views'] = total_views_count
    data['total_likes'] = total_likes_count
    data['followers'] = followers_list
    data['following'] = following_list
    data['posts'] = posts_list
    
    result['data'] = data

    return result
