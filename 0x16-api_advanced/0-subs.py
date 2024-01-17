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
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    req = requests.get(url, headers=headers)

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
