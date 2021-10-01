#!/bin/
"""
Solution to this problem:
https://www.hackerrank.com/challenges/linkedin-practice-graph-theory-bfs/problem
"""#!/bin/python3

import math
import os
import random
import re
import sys
import unittest


def compareTriplets(a, b):
    comparison_points = [0, 0]
    for score_a, score_b in zip(a, b):
        if score_a > score_b:
            comparison_points[0] += 1
        elif score_b > score_a:
            comparison_points[1] += 1

    return comparison_points

    
class TestCompareTriplets(unittest.TestCase):
    def test_compare_triplets_1(self):
        a = [3, 2, 1]
        b = [1, 2, 3]
        
        result = compareTriplets(a, b)
        expected = [1, 1]
        self.assertEqual(result, expected)
   
    def test_compare_triplets_2(self):
        a = [3, 3, 3]
        b = [1, 1, 1]
        
        result = compareTriplets(a, b)
        expected = [3, 0]
        self.assertEqual(result, expected)
   
    def test_compare_triplets_3(self):
        a = [2, 2, 2]
        b = [2, 2, 2]
        
        result = compareTriplets(a, b)
        expected = [0, 0]
        self.assertEqual(result, expected)
        
        
#unittest.main()

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

