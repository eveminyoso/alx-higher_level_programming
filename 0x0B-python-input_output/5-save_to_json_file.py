#!/usr/bin/python3
"""Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes json object to a text file"""

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
