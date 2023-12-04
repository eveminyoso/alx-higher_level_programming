#!/usr/bin/python3
""" adds a new attribute"""


def add_attribute(obj, attr_name, attr_value):
    """ adds a new attribute to an object"""

    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("Can't add new attribute to non-object")
