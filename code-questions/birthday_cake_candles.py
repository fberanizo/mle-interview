#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
"""

import collections
import math
import os
import random
import re
import sys
import unittest

def birthdayCakeCandles(candles):
    counter = collections.defaultdict(int)
    maximum = -1
    for candle in candles:
        counter[candle] += 1
        if candle > maximum:
            maximum = candle
    return counter[maximum]

class TestBirthdayCakeCandles(unittest.TestCase):
    
    def test_all_candle_are_4(self):
        candles = [4, 4, 4, 4]
        result = birthdayCakeCandles(candles)
        expected = 4
        self.assertEqual(result, expected)
        
    def test_single_maximum_candle_is_5(self):
        candles = [4, 4, 4, 5]
        result = birthdayCakeCandles(candles)
        expected = 1
        self.assertEqual(result, expected)

#unittest.main(verbosity=2)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
