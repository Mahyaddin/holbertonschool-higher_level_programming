#!/usr/bin/python3
""" Fetches and prints posts from a JSON API using requests """
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Fetched {} posts".format(len(response.json())))
        for post in response.json()[:3]:  # İlk 3 postu göstərək
            print(post.get('title'))
    else:
        print("Fetch fail")
