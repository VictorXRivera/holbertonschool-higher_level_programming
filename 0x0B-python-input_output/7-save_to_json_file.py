#!/usr/bin/python3
""" Saving to json file """
import json


def save_to_json_file(my_obj, filename):
    obj = json.dumps(my_obj)
    with open(filename, "w") as file:
        return file.write(obj)
