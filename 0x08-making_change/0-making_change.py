#!/usr/bin/python3
"""
Determining the fewest number of coins needed to meet a given
amount of total.
"""


def makeChange(coins, total):
    """
    Making changes from wthin.

    Args:
        coins - list of the values of the coins in your possession.
        total - amount of the coins

    Returns:
        fewest number of coins needed to meet total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        count += total // coin
        total %= coin
    return count if total == 0 else -1
