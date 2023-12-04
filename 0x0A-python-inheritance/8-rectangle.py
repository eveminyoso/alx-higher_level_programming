#!/usr/bin/python3
"""raise error class"""


class BaseGeometry:
    """Exeception error handling"""

    def area(self):
        """Error handling"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate function"""

        self.name = name
        self.value = value

        if not (isinstance(self.value, int)):
            raise TypeError(f"{name}  must be an integer")
        if self.value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """initialising this mehod"""

    def __init__(self, width, height):
        """constructor"""

        self.__width = 0  # Initialize as 0 before validation
        self.__height = 0  # Initialize as 0 before validation
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
