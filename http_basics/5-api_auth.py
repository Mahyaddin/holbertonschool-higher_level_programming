#!/usr/bin/python3
""" API request with Basic Authentication """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = "https://api.github.com/user"
        user = sys.argv[1]
        pwd = sys.argv[2]
        r = requests.get(url, auth=(user, pwd))
        print(r.json().get('id'))
