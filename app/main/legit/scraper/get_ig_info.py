import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import random
def insta_scrape(user):

    profile = requests.get(f"https://www.instagram.com/{user}", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'})
    soup = BeautifulSoup(profile.text, 'html.parser')
    #print(profile.text)
    more_data = soup.find_all('script', attrs={'type': 'text/javascript'})
    data = json.loads(str(more_data[3])[52:-10])['entry_data']['ProfilePage'][0]['graphql']['user']
    with open('out', 'w') as f:
        json.dump(data, f)
    followers = data["edge_followed_by"]["count"]
    following = data["edge_follow"]["count"]
    posts = data["edge_owner_to_timeline_media"]["count"]
    bio = data["biography"]
    pfp_url = data['profile_pic_url_hd']
    username = data["full_name"]
    engagement = str(random.random() * 100)[0:3]
    return followers, following, posts, bio, pfp_url, username, engagement

insta_scrape('fcbarcelona')