#!/usr/bin/python3

"""
 queries the Reddit API and returns the number of subscribers
"""

import requests
import json


def number_of_subscribers(subreddit):
    """
    documentation
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
