#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for element in sorted(a_dictionary.items()):
        print(element[0], ":", element[1])
