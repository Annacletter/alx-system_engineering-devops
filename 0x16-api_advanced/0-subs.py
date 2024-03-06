#!/usr/bin/python3
"""
    Script for querying the Reddit API to fetch the number


def number_of_subscribers(subreddit):
    """
    Function to query the Reddit API and return the number of subscriber
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit.
    """
    # Construct the URL for the subreddit's information
    url = "https://api.reddit.com/r/{}/about".format(subreddit)

    # Define custom User-Agent header
    headers = {'User-Agent': 'CustomClient/1.0'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return 0

    # Parse the JSON response
    json_response = response.json()

    # Check if the 'data' key exists in the response
    if 'data' in json_response:
        # Extract the number of subscribers from the response data
        return json_response["data"].get("subscribers", 0)
    else:
        return 0
