#!/usr/bin/python3
"""
Module for printing a square
>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    Prints a square of size

    Parameters:
    size(int) - length of the square

    prints - the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(0, size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testmod("./tests/4-print_square.txt")
