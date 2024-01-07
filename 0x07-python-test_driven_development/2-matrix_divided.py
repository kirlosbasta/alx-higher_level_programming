#!/usr/bin/python3
"""Matrix divide module contain one function
    matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """Return new list of divided elements of a matrix by div

    Args:
        matrix: List of list of int and floats
        div: int or float execpt zero
    """
    not_list = 'matrix must be a matrix (list of lists) of integers/floats'
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
        raise TypeError(not_list)
    for raw in matrix:
        if not isinstance(raw, list):
            raise TypeError(not_list)
        length = len(matrix[0])
        if len(raw) != length:
            raise TypeError('Each row of the matrix must have the same size')
        for element in raw:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError(not_list)
    return [[round(element/div, 2) for element in raw] for raw in matrix]
