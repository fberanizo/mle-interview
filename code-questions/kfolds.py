import random
import unittest

# Ensures shuffle operations are deterministic
random.seed(20211015)


def k_folds(array, n):
    """
    Yields arrays of training_fold, test_fold given an array of indices and an integer K.

    Parameters
    ----------
    indices : List[int]
    k : int

    Yields
    ------
    Tuple[List, List]
    """
    random.shuffle(array)
    start_index = 0
    step = len(array) // n
    for start_index in range(0, step * n, step):

        test_fold = array[start_index:start_index + step]
        training_fold = array[0:start_index] + array[start_index + step:]

        yield training_fold, test_fold
        start_index += step


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    for folds in k_folds(array, n):
        print(folds)



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

        result = k_folds(indices, K)
        expected = [[2, 3], [1], [3], [1, 2]]

        self.assertEqual(result, expected)

    def test_solution_k_3(self):
        """
        Simple test case K = 3.
        """
        indices = [1, 2, 3, 4, 5]
        K = 3

        result = k_folds(indices, K)
        expected = [[1, 2], [3, 4, 5], [3, 4], [1, 2, 5], [5], [1, 2, 3, 4]]

        self.assertEqual(result, expected)
