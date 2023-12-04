#!/usr/bin/python3
"""prints sorted list"""


class MyList(list):
    """inherits list"""

    def print_sorted(self):
        """returns a sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod("./tests/1-my_list.txt")
