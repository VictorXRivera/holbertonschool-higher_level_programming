#!/usr/bin/python3
def uppercase(str):
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) <= 123:
            letter = chr(ord(str[char]) - 32)
        else:
            letter = chr(ord(str[char]))
        print("{:s}".format(letter), end="")
    print("")
