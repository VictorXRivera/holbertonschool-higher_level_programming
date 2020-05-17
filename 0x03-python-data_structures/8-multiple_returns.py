#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return None
    for char in sentence[0]:
        if char == 0:
            return None
        else:
            return length, char
