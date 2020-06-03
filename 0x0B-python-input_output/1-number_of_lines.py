#!/usr/bin/python3
""" Function that returns number of lines """


def number_of_lines(filename=""):
    """ Number of lines """
    number = 0
    line = 0
    with open(filename) as f:
        for number, line in enumerate(f):
            pass
    return number + 1
