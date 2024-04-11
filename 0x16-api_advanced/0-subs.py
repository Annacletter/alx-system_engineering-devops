#!/usr/bin/python3
"""
    Queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
        Queries the Reddit API and returns the number
        of subscribers for a given subreddit.
        @param subreddit: Name of the subreddit
        @return: Number of subscribers, or "KO" if subreddit not found or error
    """
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'CustomClient/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()
        if 'data' in data:
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
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

