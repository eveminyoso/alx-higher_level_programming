#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    return [i % 2 == 0 for i in new_list]
