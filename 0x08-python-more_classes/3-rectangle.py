#!/usr/bin/python3
"""Module for printing a square"""


class Rectangle:
    """
    width assigninment

    returns:
    the size
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """
    width assigninment

    returns:
    the size
    """
    @property
    def width(self):
        return self.__width
    """
    width assigninment

    returns:
    the size
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """
    width assigninment

    returns:
    the size
    """
    @property
    def height(self):
        return self.__height
    """
    width assigninment

    returns:
    the size
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """
    width assigninment

    returns:
    the size
    """
    def area(self):
        return self.__width * self.__height
    """
    width assigninment

    returns:
    the size
    """
    def perimeter(self):
        return 2 * (self.__width + self.__height)
    """
    width assigninment

    returns:
    the size
    """
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for i in range(self.__height):
                result += '#' * self.__width + '\n'
            return result.rstrip()
