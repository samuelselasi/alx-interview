#!/usr/bin/python3
"""Module to solve Prime Game using Sieve of Eratosthenes Algorithm"""


def isWinner(x, nums):
    """Function to determine winner of Prime Game"""

    if not nums or x < 1:
        return None

    max_limit = max(nums)
    is_prime = [True for _ in range(max(max_limit + 1, 2))]

    for i in range(2, int(pow(max_limit, 0.5)) + 1):
        if not is_prime[i]:
            continue

        for j in range(i*i, max_limit + 1, i):
            is_prime[j] = False

    is_prime[0] = is_prime[1] = False
    cumulative_primes = 0

    for i in range(len(is_prime)):
        if is_prime[i]:
            cumulative_primes += 1
        is_prime[i] = cumulative_primes

    winner = ''
    score = 0

    for n in nums:
        score += is_prime[n] % 2 == 1

    if score * 2 == len(nums):
        winner = None
    if score * 2 > len(nums):
        winner = "Maria"
    else:
        winner = "Ben"

    return winner
