#!/usr/bin/python3
""" Easier Error request script """

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r is not None:
        if r.status_code == requests.codes.ok:
            print(r.text)
        else:
            print('Error code: {}'.format(r.status_code))
