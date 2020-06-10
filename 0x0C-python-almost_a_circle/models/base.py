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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Json string to file """
        if list_objs is None:
            list_objs = []
        d_list = []
        for key in list_objs:
            d_list.append(cls.to_dictionary(key))
        j_list = Base.to_json_string(d_list)
        if cls.__name__ == "Rectangle":
            filename = "Rectangle.json"
        else:
            filename = "Square.json"
        with open(filename, "w") as f:
            f.write(j_list)
