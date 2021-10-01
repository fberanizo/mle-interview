#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/mini-max-sum/problem
"""

import math
import os
import random
import re
import sys
import unittest

def findMiniMaxSum(arr):
    sum_ = 0
    minimum, maximum = -1, -1

    for number in arr:
        sum_ += number
        if number < minimum or minimum == -1:
            minimum = number
            
        if number > maximum:
            maximum = number
            
    return minimum, maximum, sum_


def miniMaxSum(arr):
    minimum, maximum, sum_ = findMiniMaxSum(arr)
            
    largest_sum = sum_ - minimum
    smallest_sum = sum_ - maximum
    
    print(" ".join(map(str, [smallest_sum, largest_sum])))

class TestFindMiniMaxSum(unittest.TestCase):
    
    def test_sequence_1_to_5(self):
        arr = [1, 2, 3, 4, 5]
        result = findMiniMaxSum(arr)
        expected = (1, 5, 15)
        self.assertEqual(result, expected)
    
    def test_sequence_5_to_1(self):
        arr = [5, 4, 3, 2, 1]
        result = findMiniMaxSum(arr)
        expected = (1, 5, 15)
        self.assertEqual(result, expected)


unittest.main(verbosity=2)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
