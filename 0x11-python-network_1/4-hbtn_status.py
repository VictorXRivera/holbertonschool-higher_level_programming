#!/usr/bin/python3
""" Using package requests """
import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    if r is not None:
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
