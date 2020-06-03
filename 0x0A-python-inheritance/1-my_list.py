#!/usr/bin/python3
""" Class defining list """


class MyList(list):
    """ Function to print sorted list """
    def print_sorted(self):
        """ Print sorted """
        my_list = list(self)
        print(sorted(my_list))
