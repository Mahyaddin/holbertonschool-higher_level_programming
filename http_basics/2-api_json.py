#!/usr/bin/python3
""" Fetches JSON data using requests """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        r = requests.get(url)
        try:
            json_data = r.json()
            print(json_data)
        except Exception:
            print("Not a valid JSON")
