#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:topten:v1.0 (by /u/fakeuser12345)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except requests.RequestException:
        print(None)

