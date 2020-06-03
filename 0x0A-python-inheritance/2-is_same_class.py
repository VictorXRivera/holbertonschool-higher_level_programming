#!/usr/bin/python3
""" function to check if object is exactly an instance of class """


def is_same_class(obj, a_class):
    """ Checks for object """
    if type(obj) is a_class:
        return True
    return False
