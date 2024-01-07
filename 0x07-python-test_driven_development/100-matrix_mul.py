#!/usr/bin/python3
"""Module that contain multiplication of two matrices"""


def matrix_mul(m_a, m_b):
    """
    return the multiplication of two matrices
    Args:
        m_a: List of list of integer and float
        m_b: List of list of integer and float
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
        elif len(m_a) == 0 or len(row) == 0:
            raise ValueError("m_a can't be empty")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')
        elif len(m_b) == 0 or len(row) == 0:
            raise ValueError("m_b can't be empty")
    for row in m_a:
        for ele in row:
            if not (isinstance(ele, int) or isinstance(ele, float)):
                raise TypeError('m_a should contain only integers or floats')
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for row in m_b:
        for ele in row:
            if not (isinstance(ele, int) or isinstance(ele, float)):
                raise TypeError('m_b should contain only integers or floats')
        if len(row) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = []
    for i in range(len(m_a)):
        row = []
        num = 0
        for j in range(len(m_b[0])):
            for x in range(len(m_a[0])):
                num += m_a[i][x] * m_b[x][j]
            row.append(num)
            num = 0
        matrix.append(row)
    return matrix
