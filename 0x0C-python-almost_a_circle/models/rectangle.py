#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """
    child class of Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializing the class with the two must attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # getter and setter for width
    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    # getter and setter for height
    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # getter and setter for x
    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x getter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # getter and setter for y
    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area"""
        if (self.width or self.height) != 0:
            x = self.width * self.height
        return x

    def display(self):
        """prints the quadrilateral"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        args assigns the arguments to parameters
        **kwargs assigns key value items, i.e dictionary items
        """
        if args is not None:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

        if kwargs:
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

    def to_dictionary(self):
        """returns a predetermined dictionary"""
        new = dict()

        new = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "width": self.width,
            "height": self.height
        }
        return new

    def __str__(self):
        """returns that :)"""
        x = f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return x
