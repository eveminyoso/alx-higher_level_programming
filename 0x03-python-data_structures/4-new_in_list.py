#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_ = my_list[:]
    len_ = len(my_list)

    if idx < 0 or idx >= len_:
        return my_list[:]
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
