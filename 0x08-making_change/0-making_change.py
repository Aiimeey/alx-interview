#!/usr/bin/python3
"""make change methods"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """ Computes the min number of coins needed to make up a given amount"""
    coins.sort(reverse=True)
    count = 0
    if not coins:
        return -1
    while total > 0:
        for x in range(len(coins)):
            if coins[x] <= total:
                total -= coins[x]
                count += 1
                break
            if x == len(coins) - 1 and coins[x] > total:
                return -1

    return count
