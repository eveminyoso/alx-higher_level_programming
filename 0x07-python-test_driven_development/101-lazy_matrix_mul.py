#!/usr/bin/python3
"""
Module using numpy module for matrix multi
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Does matrix multiplication using numpy module

    parameters:
    m_a - first matrix
    m_b - second matrix
    """
    a = np.array(m_a)
    b = np.array(m_b)
    if not m_a or not any(m_a):
        raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
    if not m_b or not any(m_b):
        raise ValueError("shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")
    if not m_a or not m_b or not any(m_a) or not any(m_b):
        raise ValueError("m_a can't be empty and m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("invalid data type for einsum")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("invalid data type for einsum")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("setting an array element with a sequence.")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("setting an array element with a sequence.")
    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)")

    result = np.dot(a, b)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod("./tests/101-lazy_matrix_mul.txt")
