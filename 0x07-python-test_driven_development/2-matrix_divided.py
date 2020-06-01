#!/usr/bin/python3
"""Function to divide matrix"""


def matrix_divided(matrix, div):
    """ divide elements of matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for index in matrix:
        if not isinstance(index, list):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for index in matrix:
        for element in index:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    length = len(matrix[0])
    for line in matrix:
        if len(line) is not length:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    div_matrix = [[round(d / div, 2) for d in index] for index in matrix]
    return div_matrix
