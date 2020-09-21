from pprint import pprint
from TikTokApi import TikTokApi

api = TikTokApi()

def tt_scrape(username):
    data = api.byUsername(username)[0]
    resp = data["author"]
    resp["authorStats"] = data["authorStats"]

    # resp["id"] = data["id"]
    # resp["username"] = username
    # resp["desc"] = data["desc"]
    # resp["createTime"]= data["createTime"]

    pprint(resp)
    return resp


tt_scrape("addisonre")