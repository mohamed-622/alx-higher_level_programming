#!/usr/bin/python3
"""Module that takes in a URL and an email, sends a POST request."""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    res = requests.post(url, data=values)
    print(res.text)
