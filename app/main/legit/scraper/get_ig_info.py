import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import random

def insta_scrape(username):
    response = requests.get(f"https://www.instagram.com/{username}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        return "User doesnt exist"
    
    scripts = soup.find_all('script')

    for s in scripts:
        try:
            content = s.contents[0]
            data_object = content[content.find('{"config"') : -1]

            # check if object exists
            if data_object != '':
                data_json = json.loads(data_object)
                break
        except Exception as e:
            print(f'Error has occurred: {e}')

    data = data_json['entry_data']['ProfilePage'][0]['graphql']['user']

    followers = data["edge_followed_by"]["count"]
    following = data["edge_follow"]["count"]
    posts = data["edge_owner_to_timeline_media"]["count"]
    bio = data["biography"]
    pfp_url = data['profile_pic_url_hd']
    username = data["full_name"]
    engagement = str(random.random() * 100)[0:3]
    return followers, following, posts, bio, pfp_url, username, engagement

