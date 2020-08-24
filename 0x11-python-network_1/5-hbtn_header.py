#!/usr/bin/python3
""" Response header value """
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r is not None:
        print(r.headers.get('X-Request-Id'))
