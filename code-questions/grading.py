#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/grading/problem
"""

import math
import os
import random
import re
import sys

def roundGrade(grade):
    if grade < 38:
        return grade
    
    remainder_to_next_multiple_of_5 = grade % 5
    
    if remainder_to_next_multiple_of_5 > 2:
        return grade + 5 - remainder_to_next_multiple_of_5
    
    return grade

def gradingStudents(grades):
    return [roundGrade(grade) for grade in grades]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
