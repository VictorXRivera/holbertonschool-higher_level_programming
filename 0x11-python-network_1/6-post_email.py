#!/usr/bin/python3
""" Using requests for POST request module """
import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    if r is not None:
        print(r.text)
