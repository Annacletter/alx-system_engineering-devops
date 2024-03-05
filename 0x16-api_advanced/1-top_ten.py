#!/usr/bin/python3
"""
Script to retrieve the top 10 hot posts from a subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first 10 hot posts.

    :param subreddit: The subreddit for which to retrieve the top posts.
    """
    url = f"https://api.reddit.com/r/{subreddit}?sort=hot&limit=10"
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    json_response = response.json()

    if 'data' in json_response:
        for post in json_response.get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
