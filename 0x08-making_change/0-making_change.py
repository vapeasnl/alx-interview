#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):
    """ return the fewest number of coins needed to meet givern amount """
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[-1] if dp[-1] != total + 1 else -1
