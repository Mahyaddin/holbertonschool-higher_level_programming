#!/usr/bin/python3
""" API request with Basic Authentication """
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://httpbin.org/basic-auth/user/pass"
    response = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))
    print(response.status_code)
