#!/usr/bin/python3

""" Function that returns number of lines """


def number_of_lines(filename=""):
    """ Number of lines """
    with open(filename) as file:
        for i, l in enumerate(file):
            pass
    file.closed
    return i + 1
