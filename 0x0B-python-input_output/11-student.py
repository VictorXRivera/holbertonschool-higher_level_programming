#!/usr/bin/python3
""" Student Class """


class Student:
    """ Instantiation """
    def __init__(self, first_name, last_name, age):
        """ Attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return json str """
        return self.__dict__