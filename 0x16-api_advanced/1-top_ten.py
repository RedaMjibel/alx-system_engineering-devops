#!/usr/bin/python3

"""
 queries the Reddit API and returns the number of subscribers
"""

import requests
import json


def top_ten(subreddit):
    """
    documentation
    """
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/elbatouri)"
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    req = requests.get(url, headers=headers, params={"limit": 10})

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
