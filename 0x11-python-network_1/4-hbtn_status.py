#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    res = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
