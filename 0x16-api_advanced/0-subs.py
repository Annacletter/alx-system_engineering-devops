#!/usr/bin/python3
"""
    Querying the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
        Queries the Reddit API and returns the number
        of subscribers.
        @param subreddit: Name of the subreddit
        @return: Number of subscribers, or 0 if subreddit not found or error
    """
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'CustomClient/1.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

