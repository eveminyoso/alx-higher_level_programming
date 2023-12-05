#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """returning pascals triagle"""

    # Check if n is less than or equal to 0
    if n <= 0:
        # If true, return an empty list
        return []

    # Initialize Pascal's triangle with the first row [1]
    triangle = [[1]]

    # Loop to generate the subsequent rows up to the nth row
    for i in range(1, n):
        # Initialize a new row with the first element as 1
        row = [1]

        # Loop to calculate the elements in the middle of the row
        for j in range(1, i):
            # Add the two numbers above to get the current number
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)

        # Add the newly generated row to the Pascal's triangle
        triangle.append(row)

    return triangle
