#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("- type:", type(html))
        print("- content:", html)
        print("- utf8 content:", html.decode("utf-8"))
