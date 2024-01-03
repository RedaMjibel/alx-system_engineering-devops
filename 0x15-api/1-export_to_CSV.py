#!/usr/bin/python3
"""
Returns information about his/her TODO list progress and
exports data in CSV format.
"""
import csv
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

    csv_rows = []

    for tasks_done in comp_json:

        task_completed = tasks_done['completed']

        task_title = tasks_done.get('title')

        csv_rows.append([idarg, name_json, str(task_completed), task_title])

        if task_completed:
            tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name_json, tasks, total_tasks))

    for tasks_done in comp_json:
        if tasks_done['completed']:
            print("\t " + tasks_done.get('title'))

    csv_filename = '{}.csv'.format(idarg)
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        csv_writer.writerows(csv_rows)

    print('Data exported to {}'.format(csv_filename))
