#!/usr/bin/python3
"""A script for analyzing word frequency in the titles of hot posts on Reddit."""


def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries the Reddit API to count occurrences of words from word_list in
    the titles of all hot posts from a given subreddit."""

    import requests

    # Fetching information about hot posts from the specified subreddit
    subreddit_info = requests.get("https://api.reddit.com/r/{}?sort=hot.json"
                                  .format(subreddit),
                                  params={"after": after},
                                  headers={"User-Agent": "My-User-Agent"},
                                  allow_redirects=False)
    if subreddit_info.status_code != 200:
        return None

    # Extracting JSON data from the response
    info = subreddit_info.json()

    # Extracting titles of hot posts
    hot_titles = [child.get("data").get("title")
                  for child in info
                  .get("data")
                  .get("children")]
    if not hot_titles:
        return None

    # Removing duplicate words from the word list
    word_list = list(dict.fromkeys(word_list))

    # Initializing the word count dictionary if not provided
    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    # Counting occurrences of words in titles
    for title in hot_titles:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    # If there are no more pages of hot posts, print the word counts
    if not info.get("data").get("after"):
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        # Recursive call to fetch and count words from the next page
        return count_words(subreddit, word_list, word_count,
                           info.get("data").get("after"))
