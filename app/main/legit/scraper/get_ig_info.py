import requests
from bs4 import BeautifulSoup
import json


def insta_scrape(user):

    profile = requests.get(f"https://www.instagram.com/{user}", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'})
    soup = BeautifulSoup(profile.text, 'html.parser')
    more_data = soup.find_all('script', attrs={'type': 'text/javascript'})
    data = json.loads(more_data[3].get_text()[21:].strip(';'))
    p_data = data['entry_data']['ProfilePage'][0]['graphql']['user']
    followers = str(p_data['edge_followed_by']['count'])
    following = str(p_data['edge_follow']['count'])
    posts = str(p_data['edge_owner_to_timeline_media']['count'])
    bio = str(p_data['biography'].replace('\n', ', '))
    pfp_url = str(p_data['profile_pic_url_hd'])
    username = str(p_data['username'])

    return followers, following, posts, bio, pfp_url, username 

