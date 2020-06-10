#!/usr/bin/python3
""" Base of all other classes """
import json


class Base:
    """ Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Using json.dumps """
        if list_dictionaries is None:
            return "[]"
        j_list = json.dumps(list_dictionaries)
        return j_list
