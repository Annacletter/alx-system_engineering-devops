#!/usr/bin/python3
"""
    Fetching hot articles from Reddit using the API.
"""
import requests


def fetch_hot_articles(subreddit, hot_list=[]):
    """
        Recursive function to retrieve hot articles from a given subreddit using the Reddit API.

        :param subreddit: The name of the subreddit to fetch hot articles from.
        :param hot_list: A list containing the titles of hot articles (optional).
        :return: A list containing the titles of hot articles.
    """
    if isinstance(subreddit, list):
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(url, subreddit[1])
    else:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]

    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    json_response = response.json()
    if 'data' in json_response:
        data = json_response.get("data")
        if not data.get("children"):
            return hot_list
        for post in data.get("children"):
            hot_list.append(post.get("data").get("title"))
        if not data.get("after"):
            return hot_list
        subreddit[1] = data.get("after")
        fetch_hot_articles(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return hot_list
    else:
        return None
