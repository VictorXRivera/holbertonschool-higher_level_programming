#!/usr/bin/python3
""" Function that returns number of lines """


def number_of_lines(filename=""):
    """ Number of lines """
    number = 0
    with open(filename) as file:
        for numbers in file:
            number += 1
    return number
