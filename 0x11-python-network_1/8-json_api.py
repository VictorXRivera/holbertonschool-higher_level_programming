#!/usr/bin/python3
""" JSON API """
from sys import argv
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    line_arg = argv[1] if len(argv) > 1 else ''
    try:
       r = requests.post(url, data={'line_arg': line_arg})
       jsoned = r.json()
       if 'id' in jsoned and 'name' in jsoned:
           print('[{}] {}'.format(jsoned['id'], jsoned['name']))
       else:
           print('No result')
    except ValueError:
        print('not a valid JSON')
