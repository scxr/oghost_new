from pprint import pprint
from TikTokApi import TikTokApi

api = TikTokApi()

def tt_scrape(username):
    resp = {}
    data = api.byUsername(username)[0]
    #  = data["author"]
    # resp["authorStats"] = data["authorStats"]

    # resp["id"] = data["id"]
    # resp["username"] = username
    # resp["desc"] = data["desc"]
    # resp["createTime"]= data["createTime"]
    resp["username"] = username
    resp["nickname"] = data["author"]["nickname"]
    resp["diggCount"] = data["authorStats"]["diggCount"]
    resp["followerCount"] = data["authorStats"]["followerCount"]
    resp["followingCount"] = data["authorStats"]["followingCount"]
    resp["heart"] = data["authorStats"]["heart"]
    resp["heartCount"] = data["authorStats"]["heartCount"]
    resp["videoCount"] = data["authorStats"]["videoCount"]
    resp["desc"] = data["desc"]
    resp["pfp_url"] = data["author"]["avatarThumb"]

    # pprint(resp)
    return resp

# 
# tt_scrape("addisonre")