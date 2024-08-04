Island Perimeter
Introduction

The Island Perimeter project is designed to test your ability to manipulate 2D arrays and apply logical reasoning to solve a geometric problem. In this project, you are required to compute the perimeter of a single island within a grid represented by a 2D array of integers. This exercise involves understanding and working with matrices, conditional logic, and perimeter calculation in Python.
Overview

The objective of this project is to develop a function, island_perimeter, which calculates the perimeter of an island within a grid. The grid is a rectangular 2D list where:

    0 represents water.
    1 represents land.

Problem Description

Given a grid:

    Each cell is square with a side length of 1.
    Cells are connected horizontally or vertically (not diagonally).
    The grid is surrounded entirely by water.
    There is only one island or no island in the grid.
    The island does not contain any lakes (water cells that are not connected to the surrounding water).

You are required to implement a function island_perimeter(grid) that returns the perimeter of the island described in the grid.
Task

    Function Signature: def island_perimeter(grid: List[List[int]]) -> int:
    Input: A 2D list grid where each element is either 0 (water) or 1 (land).
    Output: An integer representing the perimeter of the island.
