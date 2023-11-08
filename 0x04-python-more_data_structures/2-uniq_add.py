#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()  # Initialize an empty set to store unique integers
    sum_unique = 0  # Initialize the sum of unique integers

    for num in my_list:
        if num not in unique_integers:
            sum_unique += num
            unique_integers.add(num)

    return sum_unique
