#!/usr/bin/python3
""" Functio writing string to file """


def write_file(filename="", text=""):
    """ Write file """
    with open(filename, 'w') as file:
        print(file.write(text))
