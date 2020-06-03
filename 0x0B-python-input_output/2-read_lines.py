#!/usr/bin/python3
""" Function to count n number of lines in file """


def read_lines(filename="", nb_lines=0):
    """ Reading lines """
    if nb_lines <= 0:
        nb_lines = 100000
    with open(filename, 'r') as file:
        for i in range(0, nb_lines):
            file_line = file.readline()
            if file_line != "":
                print(file_line, end="")
            else:
                break
