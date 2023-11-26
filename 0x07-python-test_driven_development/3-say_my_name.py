#!/usr/bin/python3
"""
Module for printing first and last name
>>> say_my_name("Alex", "Delei")
My name is Alex Delei
"""


def say_my_name(first_name, last_name=""):
        """
        Prints first or last name

        Parameters:
        first_name(str) - the first name duuh
        last_name(str) - the last name bruv

        prints the names
        """
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        print("My name is {} {}".format(first_name, last_name))


        if __name__ == "__main__":
            import doctest
            doctest.testmod("./tests/3-say_my_name.txt")
