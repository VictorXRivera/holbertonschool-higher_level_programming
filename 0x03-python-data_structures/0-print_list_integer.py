#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num, value in enumerate(my_list, 1):
        print("{}".format(num, value))
