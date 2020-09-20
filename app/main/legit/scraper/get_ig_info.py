import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
def insta_scrape(username):
    resp = requests.get(f'https://socialstats.info/report/{username}/instagram')
    soup = BeautifulSoup(resp.content)
    vals_nums = soup.findAll("p", {"class":"report-header-number"})
    vals_info = soup.findAll("img", {"class":"img-responsive rounded-circle instagram-avatar"})
    pfp_url = vals_info[0]["src"]
    username = vals_info[0]["alt"]
    followers = str(vals_nums[0].contents[0])
    posts = str(vals_nums[1].contents[0])
    engagement = vals_nums[2].contents[0].strip()
    resp = {"followers":followers,
            "post_count": posts,
            "engagement":engagement,
            "pfp_url":pfp_url,
            "actual_name":username}

    resp = json.dumps(resp)
    return followers, posts, engagement, pfp_url, username