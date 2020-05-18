#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print(*my_list, sep='')
    if x < 0:
        return None
    else:
        return x
    try:
        safe_print_list()
    except:
        return
