#!/usr/bin/python3
"""reads a text file"""


def read_file(filename=""):
    """reads and prints contents of file"""

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
