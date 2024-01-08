#!/usr/bin/python3
"""Module for lazy matrix multiplication"""


def lazy_matrix_mul(m_a, m_b):
    """
    return the matrix product
    Args:
        m_a: List of list of integer and float
        m_b: List of list of integer and float
    """
    import numpy as np
    return np.matmul(m_a, m_b)
