#!/usr/bin/python3
""" function to check if object is exactly an instance of class """


def is_same_class(obj, a_class):
    """ Checks for object """
    if issubclass(a_class, int):
        return True
        if isinstance(obj, int):
            return True
        return False
    return False
