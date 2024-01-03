#!/usr/bin/python3
"""
returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    mysession = requests.Session()
    idarg = argv[1]
    idurl = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idarg)
    nameurl = 'https://jsonplaceholder.typicode.com/users/{}'.format(idarg)

    empid = mysession.get(idurl)
    empname = mysession.get(nameurl)

    comp_json = empid.json()
    name_json = empname.json()['name']

    tasks = 0
    total_tasks = len(comp_json)

    for tasks_done in comp_json:
        if tasks_done['completed']:
            tasks = tasks + 1

    print("Employee {} is done with tasks ({}/{}):".
          format(name_json, tasks, total_tasks))

    for tasks_done in comp_json:
        if tasks_done['completed']:
            print("\t " + tasks_done.get('title'))
