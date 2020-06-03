#!/usr/bin/python3
""" Function to check if the object is an instance 
of a class that inherited (directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """ Checks for object """
    if issubclass(int, a_class) is obj:
        return True
    return False
