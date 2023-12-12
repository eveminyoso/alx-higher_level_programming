#!/usr/bin/python3
"""
Parent class
Performs varoius functions
with various class methods
"""
import json


class Base:
    """
    Parent Class performing cool stuff
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class initialization
        increments id by 1 if no id value
        given
        """
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a jsonified list
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves json object to a file
        cool stuff
        """
        if list_objs is None:
            list_objs = []

        x = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        file = f"{cls.__name__}.json"

        with open(file, 'w', encoding="utf-8") as f:
            f.write(x)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts jsonified object to normal object
        """
        if json_string is None:
            return "[]"
        x = []
        x = json.loads(json_string)
        return x

    @classmethod
    def update(self, *args, **kwargs):
        """
        kwargs Assigns arguments to parameters
        **kwargs assigns dictionary values i.e
        key - value
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

    @classmethod
    def create(cls, **dictionary):
        """
        returns a dummwy dictionary
        """
        dummy = cls(3, 4)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        converts a jsonified string in a file back
        and creates a dictionary for it.
        """
        file = f"{cls.__name__}.json"
        try:
            with open(file, 'r', encoding="utf-8") as f:
                data = f.read()

                if not data:
                    return []
                list_dict = json.loads(data)
                return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        converts list to json object and
        stores it in a csv file
        """
        if list_objs is None:
            list_objs = []

        x = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        file = f"{cls.__name__}.csv"
        with open(file, 'w', encoding="utf-8") as f:
            f.write(x)

    @classmethod
    def load_from_file_csv(cls):
        """
        reads the data from a csv file
        and converts back the jsonified object
        """
        file = f"{cls.__name__}.csv"
        try:
            with open(file, 'r', encoding="utf-8") as f:
                data = f.read()

                if not data:
                    return []
                list_dict = json.loads(data)
                return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []
