#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
"""

import math
import os
import random
import re
import sys
import unittest

def splitHour(s):
    hour = s[:2]
    minutes_and_seconds = s[2:-2]
    am_or_pm = s[-2:]
    return int(hour), minutes_and_seconds, am_or_pm

def isAm(s):
    am_or_pm = s[-2:]
    return am_or_pm == "AM"

def isPm(s):
    am_or_pm = s[-2:]
    return am_or_pm == "PM"


def timeConversion(s):
    hour, minutes_and_seconds, am_pm = splitHour(s)
    
    if hour == 12 and isAm(s):
        hour = 0
        
    if hour != 12 and isPm(s):
        hour += 12
        
    hour = str(hour).zfill(2)

    military_hour = f"{hour}{minutes_and_seconds}"
    return military_hour


class TestSplitHour(unittest.TestCase):
    def test_12am(self):
        s = "12:00:00AM"
        
        result = splitHour(s)
        
        expected = 12, ":00:00", "AM"
        self.assertEqual(result, expected)
        
    def test_08pm(self):
        s = "08:00:00PM"
        
        result = splitHour(s)
        
        expected = 8, ":00:00", "PM"
        self.assertEqual(result, expected)

        
class TestIsAM(unittest.TestCase):
    def test_12am(self):
        s = "12:00:00AM"
        
        result = isAm(s)
        
        expected = True
        self.assertEqual(result, expected)

    def test_12pm(self):
        s = "12:00:00PM"
        
        result = isAm(s)
        
        expected = False
        self.assertEqual(result, expected)


#unittest.main(verbosity=2)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
