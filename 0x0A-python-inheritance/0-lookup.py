#!/usr/bin/python3
"""
function that returns the list of 
available attributes and methods of an object
"""

def lookup(obj):
    """ Return list of objects and methods """
    return dir(obj)
