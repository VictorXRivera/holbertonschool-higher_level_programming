#!/usr/bin/python3
""" Class to json """
import json


def class_to_json(obj):
    """ Class to json """
    jsonStr = json.dumps(obj.__dict__)
    return jsonStr
