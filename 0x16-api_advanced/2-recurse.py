#!/usr/bin/python3
"""
    quering the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
        Queries the Reddit API and returns a list
        containing the titles of all hot articles.
    """
    if type(subreddit) is list:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(url, subreddit[1])
    else:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]

    header = {'User-Agent': 'CustomClient/1.0'}
    request = requests.get(url, headers=header, allow_redirects=False)

    if request.status_code != 200:
        return None
    jreq = request.json()
    if 'data' in jreq:
        jdata = jreq.get("data")
        if not jdata.get("children"):
            return (hot_list)
        for hpost in jdata.get("children"):
            hot_list += hpost.get("data").get("title")
        if not jdata.get("after"):
            return hot_list
        subreddit[1] = jdata.get("after")
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return hot_list
    else:
        return None
