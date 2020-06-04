#!/usr/bin/python3
""" Function to load from json """
import json


def load_from_json_file(filename):
    """ Code """
    with open(filename) as file:
        return json.loads(file.readline())
