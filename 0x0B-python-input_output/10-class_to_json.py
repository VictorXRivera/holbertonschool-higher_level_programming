#!/usr/bin/python3
""" Class to json """


def class_to_json(obj):
    """ Class to json """
    jsonStr = obj.__dict__
    return jsonStr
