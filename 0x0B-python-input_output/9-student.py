#!/usr/bin/python3
"""a students class"""


class Student:
    """retrieving a dictionary"""

    def __init__(self, first_name, last_name, age):
        """class inititalization"""
        self.f_name = first_name
        self.l_name = last_name
        self.age = age

    def to_json(self):
        stud_dict = {
                "first_name": self.f_name,
                "last_name": self.l_name,
                "age": self.age
                }
        return stud_dict
