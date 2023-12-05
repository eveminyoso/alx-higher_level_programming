#!/usr/bin/python3
"""an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """an Object from a JSON file"""

    with open(filename, 'r', encoding="utf-8") as f:
        js_data = json.load(f)

    return js_data
