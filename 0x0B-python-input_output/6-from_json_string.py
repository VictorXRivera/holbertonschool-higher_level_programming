#!/usr/bin/python3
""" From json string """
import json


def from_json_string(my_str):
    """ using json.loads """
    string = json.loads(my_str)
    return string
