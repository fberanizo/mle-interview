#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/new-year-chaos/problem
"""

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(queue: List[int]):
    """
    Determine the minimum number of bribes that took place to get to a given queue order.
    
    The idea is to implement a bubble-sort like algorithm, and count swaps.
    """
    bribe_count = 0
    queue_length = len(queue)
    
    # A naive implementation of bubble sort is always O(n) = n^2
    # But this implementation is a bit smarter and ends the outer loop
    # when a whole pass occurs without a swap
    i = queue_length
    while i > 0:
        person_bribe_count, new_i = 0, 0
        for j in range(1, queue_length):
            # when a person is out of its position, then count one bribe
            if q[j-1] > q[j]:
                q[j-1], q[j] = q[j], q[j-1]
                person_bribe_count += 1
                bribe_count += 1
                
                new_i = j

                if person_bribe_count > 2:
                    print('Too chaotic')
                    return
            else:
                person_bribe_count = 0
        i = new_i

    print(bribe_count)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
