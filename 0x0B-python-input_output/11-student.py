#!/usr/bin/python3
"""student definition"""


class Student:
    """returns the key and value"""

    def __init__(self, first_name, last_name, age):
        """Class initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get value from dictionary"""

        student_dict = {}
        if attrs and isinstance(attrs, list):
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
        else:
            student_dict = vars(self)

        return student_dict

    def reload_from_json(self, json):
        """setting new attributes for class"""

        for key, value in json.items():
            setattr(self, key, value)
