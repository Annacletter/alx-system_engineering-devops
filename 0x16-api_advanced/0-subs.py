#!/usr/bin/python3
"""
    Queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
        Queries Reddit API and returns "OK" if the subreddit exists,else "KO".
        @param subreddit: Name of the subreddit
        @return: "OK" if subreddit exists, "KO" otherwise
    """
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'CustomClient/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return "OK"
        else:
            return "KO"
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "KO"


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print(number_of_subscribers(sys.argv[1]))
