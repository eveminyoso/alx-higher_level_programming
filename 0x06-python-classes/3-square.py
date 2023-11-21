#!/usr/bin/python3
"""Module representing a square"""


class Square:
    """
    This class represents a square

    Attributes:
     __size (int): Private instance attribute representing its size.
    """
    def __init__(self, size=0):
        """
        initializes a square of optional size

        Parameters:
         size (int): The size of the square (default is 0).

        Raises:
         TypeError: If size is not an integer.
         ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
         int - the area of a square
        """
        return self.__size ** 2
