#!/usr/bin/python3
""" Python script that returnes the id of a github user"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    password = sys.argv[2]
    res = requests.get(url, auth=(user, password))
    print(res.json().get("id"))
