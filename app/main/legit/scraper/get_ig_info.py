import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import random

from igramscraper.instagram import Instagram

instagram = Instagram()

# authentication supported
# instagram.with_credentials()
# instagram.login()

#Getting an account by id
# account = instagram.get_account_by_id(3)
def insta_scrape(username):
    account = instagram.get_account(username)
    
    followers = account.followed_by_count
    following =  account.follows_count
    posts = account.media_count
    bio = account.biography
    pfp_url = account.get_profile_picture_url()
    username = account.username


    # followers = data["edge_followed_by"]["count"]
    # following = data["edge_follow"]["count"]
    # posts = data["edge_owner_to_timeline_media"]["count"]
    # bio = data["biography"]
    # pfp_url = data['profile_pic_url_hd']
    # username = data["full_name"]
    engagement = str(random.random() * 100)[0:3]
    return followers, following, posts, bio, pfp_url, username, engagement



# def insta_scrape(username):
#     response = requests.get(f"https://www.instagram.com/{username}")
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#     else:
#         return "User doesnt exist"
    
#     scripts = soup.find_all('script')

#     for s in scripts:
#         try:
#             content = s.contents[0]
#             data_object = content[content.find('{"config"') : -1]

#             # check if object exists
#             if data_object != '':
#                 data_json = json.loads(data_object)
#                 break
#         except Exception as e:
#             print(f'Error has occurred: {e}')

#     print(data_json)
#     data = data_json['entry_data']['ProfilePage'][0]['graphql']['user']

#     followers = data["edge_followed_by"]["count"]
#     following = data["edge_follow"]["count"]
#     posts = data["edge_owner_to_timeline_media"]["count"]
#     bio = data["biography"]
#     pfp_url = data['profile_pic_url_hd']
#     username = data["full_name"]
#     engagement = str(random.random() * 100)[0:3]
#     return followers, following, posts, bio, pfp_url, username, engagement

