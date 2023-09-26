#!/usr/bin/python3
"""A script that computes the Pascal's triangle of a given number"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    # initialize list to store Pascal's triangle
    triangle = []

    # check if n is less than or equal to zero and return empty list
    if n <= 0:
        return triangle

    # loop through n and initialize list to store numbers
    for i in range(n):
        row = []

        # loop through previous loop and append 1 if first or last element
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)

            # if not first or last take sum of both
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # add the sum to the triangle
        triangle.append(row)

    return triangle
