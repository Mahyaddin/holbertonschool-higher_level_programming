#!/usr/bin/python3
""" Uses GitHub API and Basic Auth to display user id """
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, token))
    try:
        json_res = r.json()
        print(json_res.get('id'))
    except Exception:
        print("None")
