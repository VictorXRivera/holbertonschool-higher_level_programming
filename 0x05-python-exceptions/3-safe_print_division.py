#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        answer = a / b
        print("Inside result: {}".format(answer))
    except ZeroDivisionError:
        return None
    finally:
        return a / b
