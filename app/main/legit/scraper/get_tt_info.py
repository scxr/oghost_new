from datetime import datetime
from pprint import pprint
import requests
from bs4 import BeautifulSoup
def get_info(username):
    resp = requests.get(f'https://www.tiktok.com/@{username}')
    soup = BeautifulSoup(resp.content)
    print(resp.content)
    following = soup.find_all("strong")

    print(following)
    #<strong title="Following">31</strong>
    #<strong title="Followers">11M</strong>
    #<strong title="Likes">142M</strong>
    #<span style="font-weight: bold;">5,700,000</span>
    #<span style="font-weight: bold;">48,800,000</span>
    #<span style="font-weight: bold;">6</span>
    #<span style="font-weight: bold;">289</span>
    #https://www.tiktok.com/@gordonramsayofficial?lang=en

    '''
    count = 20
    # count and list all of the posts for a given user with the pager
    total = 0

    pager = api.getUserPager(username, page_size=count)

    for page in pager:
        total += len(page)

    print('{} has {} posts'.format(username, total))
    user = api.getUserObject(username)
    user['total_posts'] = total
    return user
    '''
get_info('fcbarcelona')

# List all of the posts for a given user after a certain date






'''
api = TikTokPy()
search = api.search_user(text="fcbarcelona")
print(search)




user = api.getUserObject("fcbarcelona")
print(dir(user))
print('#############################################')
print(user)

=import requests

def download_no_wm(url, get_bytes=1):
    url = url.split("?")[0]
    base_url = "https://savevideo.ninja/wp-admin/admin-ajax.php?action=wppress_tt_download&url={}&key=no-watermark".format(url)
    if get_bytes == 1:
        r = requests.get(base_url)
        return r.content
    else:
        return base_url
'''