#!/usr/bin/python3
""" Appending text to file """


def append_write(filename="", text=""):
    """ Append write """
    with open(filename, "a") as file:
        return file.write(text)
