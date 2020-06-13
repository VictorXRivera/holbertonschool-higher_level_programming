#!/usr/bin/python3
""" matrix multiplication """


def matrix_mul(m_a, m_b):
    """ matrix mul function"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for ele in m_a:
        if type(ele) is not list:
            raise TypeError("m_a must be a list of lists")
    for ele in m_b:
        if type(ele) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) is 0 or len(m_a[0]) is 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) is 0 or len(m_b[0]) is 0:
        raise ValueError("m_b can't be empty")

    for ele in m_a:
        for index in ele:
            if type(index) is not int and type(index) is not float:
                    raise TypeError("m_a should contain only \
integers or floats")
    for ele in m_b:
        for index in ele:
            if type(index) is not int and type(index) is not float:
                    raise TypeError("m_b should contain only \
integers or floats")

    len_a = len(m_a[0])
    len_b = len(m_b[0])
    for size in m_a:
        if len(size) is not len_a:
            raise TypeError("each row of m_a must be of the same size")
    for size in m_b:
        if len(size) is not len_b:
            raise TypeError("each row of m_b must be of the same size")

    if len_a is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = [[0 for i in range(0, len_b)] for j in range(0, len(m_a))]

    for row in range(0, len(m_a)):
        for num in range(0, len(new_matrix[0])):
            for n_a in range(0, len_a):
                new_matrix[row][num] += m_a[row][n_a] * m_b[n_a][num]
    return new_matrix
