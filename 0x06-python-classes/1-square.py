#!/usr/bin/python3
"""Class representing a square class"""


class Square:
    """
    this represents a square

    Attributes:
     size (int):Private instance attribute representing the size of the square

    """

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Parameters:
         size (int): The size of the square.
        """
        self.__size = size
