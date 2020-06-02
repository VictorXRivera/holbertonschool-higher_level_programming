#!/usr/bin/python3
""" Function to check is kind of class """
def is_kind_of_class(obj, a_class):
    """ Checks for kind of class """
    if isinstance(obj, a_class):
        return True
    return False
