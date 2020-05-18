#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        x = int(x)
        return x
        for i in my_list:
            print("{}".format(my_list[i - 1]))
    except ValueError:
        return
