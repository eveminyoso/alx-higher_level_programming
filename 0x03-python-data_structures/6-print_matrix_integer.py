#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        for idx, j in enumerate(i):
            print("{:d}".format(j), end="")
            if idx != len(i) - 1:
                print(" ", end="")
        print()
