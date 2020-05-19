#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        result = [l1, l2 in zip(my_list_1, my_list_2)]
    except ValueError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError: 
        if my_list_1 < len(list_length) or my_list_2 < len(list_length):
            print("out of range")
    finally:
        return zip(my_list_1, my_list_2)
