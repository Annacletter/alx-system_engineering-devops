#!/usr/bin/python3
"""
    quering the Reddit API
"""
import requests


def top_ten(subreddit):
    """
        Queries the Reddit API and prints the first 10 hot posts
        @subreddit: suscriptors
    """
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    request = requests.get(url, headers=header, allow_redirects=False)

    if request.status_code != 200:
        print(None)
        return
    jreq = request.json()

    if 'data' in jreq:
        for hpost in jreq.get("data").get("children"):
            print(hpost.get("data").get("title"))
    else:
        print(None)
