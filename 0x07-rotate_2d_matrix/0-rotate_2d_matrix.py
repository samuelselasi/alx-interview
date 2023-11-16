#!/usr/bin/python3
"""Module that rotates a 2-D matrix by 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Function that rotates a 2-D matrix by 90 degrees clockwise"""

    length = len(matrix)

    for row in range(int(length / 2)):
        offset = 0
        i = length - 1 - row

        for column in range(row, length - 1 - row):
            top = matrix[row][column]
            matrix[row][column] = matrix[i - offset][row]
            matrix[i - offset][row] = matrix[i][i - offset]
            matrix[i][i - offset] = matrix[column][i]
            matrix[column][i] = top

            offset += 1
