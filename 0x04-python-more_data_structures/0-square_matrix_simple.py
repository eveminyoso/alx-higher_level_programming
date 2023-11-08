#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        new_row = []

        for element in row:
            squared_value = element ** 2
            new_row.append(squared_value)

        result.append(new_row)

    return result
