#!/usr/bin/python3
"""Function to divide matrix"""


def matrix_divided(matrix, div):
    """ Returning a divided matrix """
    div_matrix = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for element in matrix:
        if type(element) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for ele2 in element:
            if type(ele2) not in [int, float]:
                raise TypeError("matrix must be a matrix (lists of lists) of integers/float")

        if len(element) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

    div_matrix = [[round(ele2 / div, 2) for ele2 in element] for element in matrix]

    return div_matrix
