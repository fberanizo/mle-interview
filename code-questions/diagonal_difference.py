#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

import math
import os
import random
import re
import sys
import unittest


def diagonalDifference(arr):
    sum_main_diagonal = 0
    sum_secondary_diagonal = 0
    for row in range(len(arr)):
        column = len(arr) - row - 1
        sum_main_diagonal += arr[row][row]
        sum_secondary_diagonal += arr[row][column]
        
    return abs(sum_main_diagonal - sum_secondary_diagonal)

class TestDiagonalDifference(unittest.TestCase):
    
    def test_diagonal_difference_zero(self):
        arr = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        
        result = diagonalDifference(arr)
        expected = 0
        self.assertEqual(result, expected)
    
    def test_diagonal_difference_larger_main_diagonal(self):
        arr = [[2, 1, 1], [1, 1, 1], [1, 1, 2]]
        
        result = diagonalDifference(arr)
        expected = 2
        self.assertEqual(result, expected)
        
    def test_diagonal_difference_larger_secondary(self):
        arr = [[1, 1, 2], [1, 1, 1], [2, 1, 1]]
        
        result = diagonalDifference(arr)
        expected = 2
        self.assertEqual(result, expected)
        
#unittest.main(verbosity=2)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
