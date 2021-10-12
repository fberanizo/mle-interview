import math
import unittest
from typing import List


def solution(indices: List[int], K: int):
    """
    Returns the arrays of folds given an array of indices and an integer K.

    Parameters
    ----------
    indices : List[int]
    k : int

    Returns
    -------
    List
    """
    rotation_size = math.ceil(len(indices) / K)

    folds = []

    test_fold_start_index = 0
    test_fold_end_index = rotation_size

    for fold_index in range(K):
        test_fold = indices[test_fold_start_index:test_fold_end_index]
        training_fold = indices[:test_fold_start_index] + indices[test_fold_end_index:]

        folds.extend([training_fold, test_fold])

        test_fold_start_index += rotation_size
        test_fold_end_index += rotation_size
    
    return folds


class TestSolution(unittest.TestCase):
    """
    Test cases that helped validating the solution.
    """
    def test_solution_k_2(self):
        """
        Simple test case K = 2.
        """
        indices = [1, 2, 3]
        K = 2

        result = solution(indices, K)
        expected = [[2, 3], [1], [3], [1, 2]]

        self.assertEqual(result, expected)

    def test_solution_k_3(self):
        """
        Simple test case K = 3.
        """
        indices = [1, 2, 3, 4, 5]
        K = 3

        result = solution(indices, K)
        expected = [[1, 2], [3, 4, 5], [3, 4], [1, 2, 5], [5], [1, 2, 3, 4]]

        self.assertEqual(result, expected)
