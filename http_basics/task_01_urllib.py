#!/usr/bin/python3
""" Fetches data from an API using urllib """
import urllib.request


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
