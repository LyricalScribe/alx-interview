#!/usr/bin/python3
"""
Determines fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """Calculates the fewest number of coins
    needed to meet the total amount"""
    if total <= 0:
        return 0

    # Sort coins in reverse order
    coins.sort(reverse=True)

    coin_count = 0
    for coin_value in coins:
        if total <= 0:
            break

        num_coins = total // coin_value
        coin_count += num_coins
        total -= num_coins * coin_value

    if total != 0:
        return -1

    return coin_count
