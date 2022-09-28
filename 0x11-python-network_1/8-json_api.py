#!/usr/bin/python3
""" send POST request to server """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sv = {"q": ""}
    else:
        sv = {"q": sys.argv[1]}
    response = requests.post("http://0.0.0.0:5000/search_user", data=sv)
    try:
        result = response.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print("Not a valid JSON")
