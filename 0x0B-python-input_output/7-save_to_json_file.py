#!/usr/bin/python3
""" Saving to json file """
import json


def save_to_json_file(my_obj, filename):
    """ Function """
    obj = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(obj)
