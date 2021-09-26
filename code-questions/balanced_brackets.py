#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/balanced-brackets/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
OPEN_BRACKET_MAP ={
    ']': '[',
    ')': '(',
    '}': '{',
}

class Stack:
    def __init__(self):
        self.stack_list = []
        
    def push(self, item):
        self.stack_list.append(item)
        
    def pop(self):
        return self.stack_list.pop()
        
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]


def isCloseBracket(c):
    return c in {'}', ')', ']'}


def isBalanced(s: str):
    """
    Returns whether  sequence of brackets is balanced.
    """
    stack = Stack()
    s_length = len(s)
    for i in range(s_length):
        bracket = s[i]

        if isCloseBracket(bracket):
            # when it is a close bracket, 
            # but there aren't any open brackets stacked
            if stack.is_empty():
                return 'NO'

            latest_open_bracket = stack.pop()

            # when it is a close bracket, 
            # but latest stacked bracket is not a match
            if latest_open_bracket != OPEN_BRACKET_MAP[bracket]:
                return 'NO'
        else:
            stack.push(bracket)

    # when the whole sequence was checked, but there are unclosed brackets
    if not stack.is_empty():
        return 'NO'
    
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
