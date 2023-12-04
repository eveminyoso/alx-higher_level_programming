#!/usr/bin/python3
"""checks for subclass return value"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class"""

    return issubclass(type(obj), a_class)
