#!/usr/bin/python3
""" Fetches data from an API using urllib """
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
