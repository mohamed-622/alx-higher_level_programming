#!/usr/bin/python3
"""Python script that displays the body of the response (decoded in utf-8)"""
import urllib
import sys

"""You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code"""

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))