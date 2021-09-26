#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/truck-tour/problem
"""
#
# 3
# 1 5
# 10 3
# 3 4

import math
import os
import random
import re
import sys


def truckTour(petrolpumps):
    """
    Finds the smallest index of the petrol pump from which we can start the tour.
    """
    start, tank = 0, 0

    for i in range(len(petrolpumps)):
        amount_of_petrol, distance_to_next_pump = petrolpumps[i]
        tank += amount_of_petrol - distance_to_next_pump
        # at any moment, if the tank is empty we find out that start position
        # should be at least in the next pump
        if tank < 0:
            start = i + 1
            tank = 0
    return start

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
