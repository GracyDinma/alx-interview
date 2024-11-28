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

    # Initialize a list to store the fewest coin
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin demoniation
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # if dp[total] is still inf, the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
