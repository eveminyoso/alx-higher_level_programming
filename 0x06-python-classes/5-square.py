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

        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
         int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        - value (int): The size of the square.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
         int - the area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#' to stdout.

        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
