#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                cnt += 1
        print()
        return cnt
    except(TypeError):
        raise IndexError
