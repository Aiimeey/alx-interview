# Coin Change Problem - Minimum Number of Coins

## Project Overview

The goal of this project is to solve the classic coin change problem, a fundamental issue in dynamic programming and greedy algorithms. The problem involves determining the minimum number of coins needed to make up a given amount using a list of available coin denominations.

## Problem Statement

Given a list of coin denominations and a total amount, your task is to compute the fewest number of coins required to achieve the specified amount. If it is not possible to make the exact amount with the given coins, return -1. If the total amount is 0 or less, return 0.

### Requirements

- **Prototype**: `def makeChange(coins, total) -> int`
- **Parameters**:
  - `coins`: A list of integers representing the coin denominations.
  - `total`: An integer representing the amount to be made up with the coins.
- **Returns**:
  - The minimum number of coins needed to meet the total amount.
  - If it is not possible to achieve the total amount with the given coins, return -1.
  - If the total amount is 0 or less, return 0.

### Constraints

- The value of each coin in the list is an integer greater than 0.
- You have an infinite number of each denomination of coin in the list.
- Your solution should be efficient and handle large inputs effectively.

## Approach

To solve the problem, you can use one of the following approaches:

1. **Greedy Algorithm**: Efficient for specific cases where the coin denominations are suitable but may not always guarantee an optimal solution.
2. **Dynamic Programming**: A more robust approach that ensures correctness by breaking down the problem into overlapping subproblems and solving them optimally.
