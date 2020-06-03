#!/usr/bin/python3
""" Class defining list """


class MyList(list):
    """ Function to print sorted list """
    def print_sorted(self):
        """ Print sorted """
        my_list = list(self)
        all(isinstance(i, int) for i in my_list)
        print(sorted(my_list))
