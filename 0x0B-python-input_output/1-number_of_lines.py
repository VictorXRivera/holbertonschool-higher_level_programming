#!/usr/bin/python3
""" Function that returns number of lines """


def number_of_lines(filename=""):
    num_lines = 0
    with open(filename, 'r') as file:
        for line in file:
            num_lines += 1
        return num_lines
