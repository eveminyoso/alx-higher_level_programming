#!/usr/bin/python3
"""Module with class square"""


class Square:
    """
    This class represents a square.

    Attributes:
    - __size (float or int): Private instance attribute representing its size.
    """

    def __init__(self, size=0):
        """
        Initializes a square with an optional size.

        Parameters:
        - size (float or int): The size of the square (default is 0).

        Raises:
        - TypeError: If size is not a number.
        - ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
        - float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        - value (float or int): The size of the square.

        Raises:
        - TypeError: If value is not a number.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        - float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare two squares for equality based on their areas.

        Parameters:
        - other (Square): Another square to compare.

        Returns:
        - bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two squares for inequality based on their areas.

        Parameters:
        - other (Square): Another square to compare.

        Returns:
        - bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compare two squares based on their areas (greater than).

        Parameters:
        - other (Square): Another square to compare.

        Returns:
        - bool: True if the area of the first square is greater.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two squares based on their areas (greater than or equal).

        Parameters:
        - other (Square): Another square to compare.

        Returns:
        - bool: True if the area of the first square is greater or equal.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compare two squares based on their areas (less than).

        Parameters:
        - other (Square): Another square to compare.

        Returns:
        - bool: True if the area of the first square is less,Falseotherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two squares based on their areas (less than or equal).

        Parameters:
        - other (Square): Another square to compare.

        Returns:
        - bool: True if the area of the first square is less or equal.
        """
        return self.area() <= other.area()
