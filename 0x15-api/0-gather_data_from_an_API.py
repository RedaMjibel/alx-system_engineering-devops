#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests as r
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"


    user = r.get(url + "users/{}".format(sys.argv[1])).json()
    todos = r.get(url + "todos", params={"userId": sys.argv[1]}).json()


    completed = [t.get("title") for t in todos if t.get("completed") is True]


    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))


    [print("\t {}".format(c)) for c in completed]
