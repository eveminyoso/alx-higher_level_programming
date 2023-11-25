#!/usr/bin/python3
"""
Module for matrix division
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 2)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
"""


def matrix_divided(matrix, div):
        """
        divides all elements of a matrix.

        Paramters:
        matrix - List of integers of floats
        div - a number

        Returns:
        a new matrix
        """
        if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if any(len(row) != len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

        return result_matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod("./test/2-matrix_divided.txt")
