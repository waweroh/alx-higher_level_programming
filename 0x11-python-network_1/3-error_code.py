#!/usr/bin/python3
""" print error code """
import urllib.request
import sys


if __name__ == "__main__":
    requ = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(requ)
        with urllib.request.urlopen(requ) as response:
            bc = response.read().decode('utf-8')
            print(bc)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
