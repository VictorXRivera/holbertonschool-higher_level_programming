#!/usr/bin/python3

""" Function that returns number of lines """


def number_of_lines(filename=""):
    """ Number of lines """
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
