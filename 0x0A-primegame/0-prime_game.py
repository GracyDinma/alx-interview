#!/usr/bin/python3
"""
A game that takes turns choosing a prime number from the set of a number.
"""


def isWinner(x, nums):
    """"
    Determines the winner of each game and returns the name of the player.
    Args:
        x: number o rounds.
        nums: list of integers representing the upper limit for each round.
    Returns:
        The number of the player with the most wins or None.
    """
    if not nums or x < 1:
        return None

    """Precompute prime numbers up to the maximum value in nums."""
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if primes[1]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False

    """ Precompute the number of primes up to each number."""
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    """ Determine the winner for each round."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
