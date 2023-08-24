#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    sorted_coins = sorted(coins, reverse=True)
    count = 0
    if total <= 0:
        return 0
    for coin in sorted_coins:
        while total >= coin:
            total -= coin
            count += 1
        if total == 0:
            return count
    return -1
