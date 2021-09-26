#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/recursive-digit-sum/problem
"""
import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def sumDigits(p: int):
    """
    Sum the digits of a given number p.
    
    Uses an efficient implementation based on integer division and remainder.
    """
    digit_sum = 0
    while p > 0:
        digit_sum += p % 10
        p //= 10
    return digit_sum

def superDigit(n: str, k: int):
    """
    Calulates the superdigit of a string representation of a number n.
    
    We define super digit of an integer  using the following rules:
    Given an integer, we need to find the super digit of the integer.
    - If x has only  digit, then its super digit is x.
    - Otherwise, the super digit of  is equal to the super digit of the sum of the digits of x.
    """
    if k == 1 and len(n) == 1:
        return int(n)
    
    # The most efficent way of solving this problem is to
    # calculate the sum of n, THEN multiply this sum by k.
    # In my first attempts, I was multiplying n by k, then calulating the sum.
    # This increases substantially the memory used and the iterations amount of iteration.
    p = sum((int(digit) for digit in str(n)), start=0)
    return superDigit(str(p * k), k=1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
