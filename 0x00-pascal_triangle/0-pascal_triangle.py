#!/usr/bin/python3
""" pascal triangle module"""


def pascal_triangle(x):
    """ pascal triangle function"""
    triangle = []
    for i in range(x):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1]+triangle[i-1][j])
        if i > 0:
            row.append(1)
        triangle.append(row)
    return triangle
