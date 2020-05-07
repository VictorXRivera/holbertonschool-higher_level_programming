#!/usr/bin/python3
def no_c(my_string):
    bad_chars = ['c', 'C']
    new_string = ''.join(i for i in my_string if i not in bad_chars)
    return new_string
