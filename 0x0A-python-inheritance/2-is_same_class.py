#!/usr/bin/python3
"""returns True if the object is instance"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance"""

    return type(obj) is a_class
