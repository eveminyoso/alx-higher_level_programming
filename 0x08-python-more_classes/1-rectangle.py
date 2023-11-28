#!/usr/bin/python3
"""Module for printing a rectangle"""


class Rectangle:
    """
    Initializing the program

    parameters:
    width (int) - the width of the rect
    height(int) - The height of the rect

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
