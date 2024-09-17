#!/usr/bin/python3
"""
0x08. Making Change
"""


def makeChange(coins, total):
    """
    Function to determine the fewest number of coins needed to meet a given
        amount total
    """
    if total <= 0:
        return 0

    length = len(coins)
    optimized = [0 for _ in range(total + 1)]

    for i in range(1, total + 1):
        smallest = float("inf")
        for j in range(length):
            if coins[j] <= i:
                smallest = min(smallest, optimized[i - coins[j]])
        optimized[i] = 1 + smallest

    if type(optimized[total]) is not int:
        return -1

    return optimized[total]
