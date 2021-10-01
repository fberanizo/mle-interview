#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/staircase/problem
"""

import math
import os
import random
import re
import sys
import unittest

def build_staircase(n):
    for hashes_count in range(1, n + 1):
        spaces_count = n - hashes_count
        staircase_level = ' ' * spaces_count + '#' * hashes_count
        yield staircase_level


def staircase(n):
    for staircase_level in build_staircase(n):
        print(staircase_level)


class TestStarcase(unittest.TestCase):
    def test_staircase_n_1(self):
        n = 1
        result = build_staircase(n)
        expected = '#'
        self.assertEqual(next(result), expected)

    def test_staircase_n_2(self):
        n = 2
        result = build_staircase(n)

        expected = ' #'
        self.assertEqual(next(result), expected)

        expected = '##'
        self.assertEqual(next(result), expected)

#unittest.main()
        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
