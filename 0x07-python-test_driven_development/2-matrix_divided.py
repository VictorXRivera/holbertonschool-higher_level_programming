#!/usr/bin/python3
"""Function to divide matrix"""


def matrix_divided(matrix, div):
    """ Returning a divided matrix """
    div_matrix = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    for element in matrix:
        if not matrix:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

        if type(element) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

        for ele in element:
            if not element:
                raise TypeError("matrix must be matrix \
(list of lists) of integers/floats")

            if type(ele) not in [int, float]:
                raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")

        if len(element) != len(matrix[0]):
            raise TypeError("Each row of the matrix must \
have the same size")
        
        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

    div_matrix = [[round(ele / div, 2) for ele in element] for element in matrix]

    return div_matrix
