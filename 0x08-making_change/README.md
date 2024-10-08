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

## Resources

- [Python Official Documentation: Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [GeeksforGeeks Articles](https://www.geeksforgeeks.org):
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to Find Minimum Number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-1-coin-change/)
- YouTube Tutorials: Look for videos on the dynamic programming approach to the coin change problem for step-by-step visual explanations.

## Testing

The provided main file (`0-main.py`) is for testing purposes and includes test cases to verify the correctness of the implementation:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Expected output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
