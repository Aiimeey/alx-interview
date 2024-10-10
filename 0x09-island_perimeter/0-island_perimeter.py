#!/usr/bin/python3
"""
Module to calculate the perimeter of an island represented in a grid
"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculate the perimeter of an island in a grid
    """
    count = 0
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if grid[i][j] == 1:
                if grid[i-1][j] == 0:
                    count += 1
                if grid[i+1][j] == 0:
                    count += 1
                if grid[i][j+1] == 0:
                    count += 1
                if grid[i][j-1] == 0:
                    count += 1
