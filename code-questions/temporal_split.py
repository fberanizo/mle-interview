import unittest
from datetime import datetime

data = [
    datetime.strptime("2021-10-10", "%Y-%m-%d"),
    datetime.strptime("2021-10-11", "%Y-%m-%d"),
    datetime.strptime("2021-10-12", "%Y-%m-%d"),
    datetime.strptime("2021-10-13", "%Y-%m-%d"),
]
training_end_date = datetime.strptime("2021-10-12", "%Y-%m-%d")


def temporal_split(data, training_end_date):
    """
    Splits temporal data into training and test datasets.

    Parameters
    ----------
    data : List
    training_end_date : datetime.datetime

    Returns
    -------
    Tuple[List, List]
    """
    training_indexes, test_indexes = [], []
    for index, date in enumerate(data):
        if date <= training_end_date:
            training_indexes.append(index)
        else:
            test_indexes.append(index)

    return training_indexes, test_indexes


class TestTemporalSplit(unittest.TestCase):

    def test_1(self):

        expected_training = [0, 1, 2]
        expected_test = [3]

        result_training, result_test = temporal_split(data, training_end_date)

        self.assertEqual(result_training, expected_training)
        self.assertEqual(result_test, expected_test)


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    training_split, test_split = temporal_split(data, training_end_date)
    print("training_split", training_split)
    print("test_split", test_split)
