#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in my_list:
        print("{:d}".format(my_list[i]), end="")
    if x < 0:
        return None
    else:
        return x
    try:
        safe_print_list_integers()
    except IndexError:
        return
