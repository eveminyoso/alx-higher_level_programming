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

        super().__init__()
        self.__width = 0  # Initialize as 0 before validation
        self.__height = 0  # Initialize as 0 before validation
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description as a string."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """initialising this mehod"""

    def __init__(self, size):
        """constructor"""

        super().__init__(size, size)  # Call the __init_
        self.__size = 0  # Initialize as 0 before validation
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Return the square description as a string."""
        return f"[Square] {self.__size}/{self.__size}"
