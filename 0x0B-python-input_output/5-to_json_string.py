#!/usr/bin/python3
""" Function to convert to json string """
import json


def to_json_string(my_obj):
    """ Using json.dumps """
    obj = json.dumps(my_obj, sort_keys=True)
    return obj
