#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the child class of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class initialization using one must value, size"""
        super().__init__(size, size, x, y, id)

    # getter and setter for size
    @property  # indicates a property method
    def size(self):
        """returns our width instance"""
        return self.width

    @size.setter
    def size(self, value):
        """assigns width and height with same value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        arguments' assignment to our parameters
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns a dictionary width our values
        """
        n = dict()

        n = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return n

    def __str__(self):
        """retuns that :) """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
