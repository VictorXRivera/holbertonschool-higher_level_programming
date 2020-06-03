#!/usr/bin/python3
import json
def to_json_string(my_obj):
    obj = json.dumps(my_obj, sort_keys=True)
    return obj
