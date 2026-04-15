#!/usr/bin/python3
"""
Interacting with a public API and saving data to CSV
"""
import requests
import csv


def fetch_and_print_posts():
    """ Fetches all posts from JSONPlaceholder and prints titles """
    url = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(url)
    print("Status Code: {}".format(r.status_code))
    
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """ Fetches all posts and saves them into a CSV file """
    url = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(url)
    
    if r.status_code == 200:
        posts = r.json()
        # Məlumatı id, title və body açarları ilə strukturlaşdırırıq
        structured_data = [
            {'id': p.get('id'), 'title': p.get('title'), 'body': p.get('body')}
            for p in posts
        ]
        
        # CSV faylına yazırıq
        with open('posts.csv', 'w', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
