#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 5
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 7
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 3
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


n = 11
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
