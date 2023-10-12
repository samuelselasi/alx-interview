#!/usr/bin/python3
"""
Module containing method that calculates fewest no. of
operations needed to result in exactly n H chars"""


def minOperations(n):
    """Function that calculates fewest no. of ops needed for n H chars"""

    operations_needed = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations_needed += divisor
            n /= divisor
        divisor += 1

    return operations_needed
