#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divided_list = [0 for number in range(0, list_length)]
    for element in range(0, list_length):
        try:
            divided_list[element] = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return divided_list
