#!/usr/bin/python3
""" print error code as the body """
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    try:
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(req.status_code))
