#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/plus-minus/problem
"""

import math
import os
import random
import re
import sys
import unittest
  
def count_positives_and_negatives(arr):
    positive_count, negative_count = 0, 0
    
    for number in arr:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
            
    return positive_count, negative_count

def calculate_plus_minus_rates(positive_count, negative_count, arr_count):
    positive_rate = positive_count / arr_count
    negative_rate = negative_count / arr_count
    zero_rate = (arr_count - positive_count - negative_count) / arr_count
    return positive_rate, negative_rate, zero_rate

    
def plusMinus(arr):
    positive_count, negative_count = count_positives_and_negatives(arr)

    arr_count = len(arr)
    positive_rate, negative_rate, zero_rate = calculate_plus_minus_rates(
        positive_count,
        negative_count,
        arr_count,
    )
    print(f"{positive_rate:.6f}")
    print(f"{negative_rate:.6f}")
    print(f"{zero_rate:.6f}")


class TestCountPositivesAndNegatives(unittest.TestCase):
    def test_positives_only(self):
        arr = [1, 1, 1]
        result = count_positives_and_negatives(arr)
        expected = (3, 0)
        self.assertEqual(result, expected)
    
    def test_negatives_only(self):
        arr = [-1, -1, -1]
        result = count_positives_and_negatives(arr)
        expected = (0, 3)
        self.assertEqual(result, expected)
    
    def test_zeroes_only(self):
        arr = [0, 0, 0]
        result = count_positives_and_negatives(arr)
        expected = (0, 0)
        self.assertEqual(result, expected)
        
    def test_mixed_values(self):
        arr = [1, -1, 0]
        result = count_positives_and_negatives(arr)
        expected = (1, 1)
        self.assertEqual(result, expected)


class TestCalculatePlusMinusRates(unittest.TestCase):
    def test_positive_only(self):
        positive_count, negative_count, arr_count = 3 ,0, 3
        result = calculate_plus_minus_rates(positive_count, negative_count, arr_count)
        expected = (1, 0, 0)
        self.assertEqual(result, expected)


#unittest.main(verbosity=2)
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
