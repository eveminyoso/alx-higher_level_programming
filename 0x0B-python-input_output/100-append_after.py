#!/usr/bin/python3
"""writes a line after a search string"""


def append_after(filename="", search_string="", new_string=""):
    """writes a line after search string"""

    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
