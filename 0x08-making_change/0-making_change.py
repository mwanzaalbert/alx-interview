#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module provides a function to determine the fewest number of coins
needed to meet a given total using a set of coin denominations.

The module contains:

makeChange: A function that implements a greedy algorithm to solve the problem.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target amount to be reached.

    Returns:
        int: The minimum number of coins needed to meet the total,
             or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    for coin in coins:
        if total == 0:
            break
        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin

    return count if total == 0 else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
