#!/usr/bin/python3
"""Module to determine the fewest no. of coins needed to meet a given total"""


def makeChange(coins, total):
    """Function to determine fewest no. of coins to meet a total"""

    if total < 1:
        return 0

    coins.sort()
    coins.reverse()

    fewest_coins = 0

    for coin_value in coins:
        if total <= 0:
            break

        coin_count = total // coin_value
        fewest_coins += coin_count
        total -= (coin_count * coin_value)

    if total != 0:
        return -1

    return fewest_coins
