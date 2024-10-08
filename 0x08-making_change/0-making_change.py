#!/usr/bin/env python3
def makeChange(coins, total):
    coins.sort(reverse=True)
    print(coins)
    count = 0
    while total > 0:
        for x in range(len(coins)):
            if coins[x] <= total:
                total -= coins[x]
                count += 1
                break
            if x == len(coins) - 1 and coins[x] > total:
                return -1

    return count
