#!/usr/bin/python3
"""
module for text formatting
"""
def text_indentation(text):
    """
    parameters: 
    text(str) - input string

    prints a text with 2 new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for char in text:
        result += char

        if char in ['.', '?', ':']:

            result += '\n\n'
            lines = [line.strip() for line in result.split('\n')]

            for line in lines:
                print(line)

if __name__ == "__main__":
    import doctest
    doctest.testmod("./test/5-text_indentation.txt")
