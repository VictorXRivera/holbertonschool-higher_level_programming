#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        value = int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
            try:
                value = float(value)
                print("{:f}".format(value))
                return True
            except ValueError:
                return False
