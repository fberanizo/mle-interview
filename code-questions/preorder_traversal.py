#!/bin/python3
"""
Solution to this problem:
https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
import unittest

def visit(root):
    values_in_preorder = [root.info]
    if root.left:
        traversed_values = visit(root.left)
        values_in_preorder.extend(traversed_values)
    if root.right:
        traversed_values = visit(root.right)
        values_in_preorder.extend(traversed_values)
    return values_in_preorder

def preOrder(root):
    values_in_preorder = visit(root)
    print(" ".join(map(str, values_in_preorder)))
    

class TestPreorderTraversal(unittest.TestCase)    :
    
    def test_visit_no_children(self):
        """
        It should return a list with a single value [1].
        """
        root = Node(info=1)

        result = visit(root)

        expected = [1]
        self.assertEqual(result, expected)

    def test_visit_one_child_left(self):
        """
        It should return a list with two values [1, 2]
        """
        root = Node(info=1)
        left = Node(info=2)
        root.left = left
        
        result = visit(root)
        expected = [1, 2]
        self.assertEqual(result, expected)
        
    def test_visit_one_child_right(self):
        """
        It should return a list with two values [1, 2]
        """
        root = Node(info=1)
        right = Node(info=2)
        root.right = right
        
        result = visit(root)
        expected = [1, 2]
        self.assertEqual(result, expected)
        
    def test_visit_two_children(self):
        """
        It should return a list with two values [1, 2, 3]
        """
        root = Node(info=1)
        left = Node(info=2)
        root.left = left
        right = Node(info=3)
        root.right = right
        
        result = visit(root)
        expected = [1, 2, 3]
        self.assertEqual(result, expected)
        
unittest.main()
        
    


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)