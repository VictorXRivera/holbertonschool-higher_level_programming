#!/usr/bin/python3
""" JSON API """
from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) < 2 or not argv[1].isalpha():
        print("No result")
    else:
        value = {'q': argv[1]}
        r = requests.post('http://0.0.0.0:5000/search_user', data=value)
        try:
            id_json = r.json().get('id')
            name_json = r.json().get('name')
            print('[{}] {}'.format(id_json, name_json))
        except:
            print("Not a valid JSON")
