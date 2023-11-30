#!/usr/bin/python3
"""
Module for an addition function
>>> add_integer(1)
99
"""


def add_integer(a, b=98):
    """
    Returns a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf'):
        raise OverflowError("Float overflow: result is infinity")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod("./tests/0-add_integer.tt")
