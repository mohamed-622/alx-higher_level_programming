#!/usr/bin/python3
"""Python script that displays the body of the response (decoded in utf-8)"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))