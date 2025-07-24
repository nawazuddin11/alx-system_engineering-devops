#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
and returns a list of all hot article titles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of all hot article titles for a given subreddit.
    Uses recursion to handle pagination.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List of titles collected so far.
        after (str): Token for the next page (for recursion).

    Returns:
        List of titles, or None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:recursivetitles:v1.0 (by /u/fakeuser12345)'}
    params = {'limit': 100, 'after': after}
    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        posts = data.get('children', [])

        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))

        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except requests.RequestException:
        return None

