#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/pairs/problem
"""

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    """
    Determine the number of pairs of array elements that have a difference equal to the target value.
    
    Uses a set to hold unique values and make it fast to check for an given value.
    """
    count = 0
    unique_items = set(arr)
    for element in unique_items:
        complement = element - k
        if complement in unique_items:
            count += 1
    return count

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
