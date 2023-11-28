#!/usr/bin/python3
"""
Module for matrix multiplication
using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    numpy module for multiplitcation
    """
    a = np.array(m_a)
    b = np.array(m_b)
    if not m_a or not any(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not any(m_b):
        raise ValueError("m_b can't be empty")
    if not m_a or not m_b or not any(m_a) or not any(m_b):
        raise ValueError("m_a can't be empty and m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("Each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("Each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(a, b)

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod("./tests/101-lazy_matrix_mul.txt")
