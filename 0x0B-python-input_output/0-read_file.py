#!/usr/bin/python3
""" reads text file and prints to stdout """


def read_file(filename=""):
    """ Function """
    with open(filename, 'r') as file:
        print(file.read(), end="")
