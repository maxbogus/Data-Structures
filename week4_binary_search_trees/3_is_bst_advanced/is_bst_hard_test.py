import unittest

from is_bst_hard import main_with_args


class MyTestCase(unittest.TestCase):
    def test_first_sample(self):
        self.assertEqual(main_with_args(3, [
            [2, 1, 2], [1, -1, -1], [3, -1, -1]
        ]), "CORRECT")

    def test_second_sample(self):
        self.assertEqual(main_with_args(3, [
            [1, 1, 2], [2, -1, -1], [3, -1, -1]
        ]), "INCORRECT")

    def test_third_sample(self):
        self.assertEqual(main_with_args(3, [
            [2, 1, 2], [2, -1, -1], [3, -1, -1]
        ]), "INCORRECT")

    def test_fourth_sample(self):
        self.assertEqual(main_with_args(3, [
            [2, 1, 2], [2, -1, -1], [3, -1, -1]
        ]), "INCORRECT")

    def test_fifth_sample(self):
        self.assertEqual(main_with_args(0), "CORRECT")

    def test_sixth_sample(self):
        self.assertEqual(main_with_args(1, [
            [2147483647, -1, -1]
        ]), "CORRECT")

    def test_seventh_sample(self):
        self.assertEqual(main_with_args(5, [
            [1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]
        ]), "CORRECT")

    def test_seventh_sample_one(self):
        self.assertEqual(main_with_args(5, [
            [1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [4, -1, -1]
        ]), "CORRECT")

    def test_seventh_sample_two(self):
        self.assertEqual(main_with_args(5, [
            [1, -1, 1], [2, -1, 2], [3, 3, 4], [4, -1, 4], [4, -1, -1]
        ]), "INCORRECT")

    def test_seventh_sample_three(self):
        self.assertEqual(main_with_args(5, [
            [1, 1, 2], [1, -1, -1], [3, 3, 4], [2, -1, 4], [3, -1, -1]
        ]), "INCORRECT")

    def test_eigth_sample(self):
        self.assertEqual(main_with_args(7, [
            [4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]
        ]), "CORRECT")

    def test_sample(self):
        self.assertEqual(main_with_args(3, [
            [2, 1, 2], [1, -1, -1], [2, -1, -1]
        ]), "CORRECT")

    def test_additional(self):
        self.assertEqual(main_with_args(7, [
            [4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [4, -1, -1], [7, -1, -1]
        ]), "CORRECT")

    def test_additional_invalid(self):
        self.assertEqual(main_with_args(7, [
            [50, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [4, -1, -1], [7, -1, -1]
        ]), "CORRECT")

    def test_additional_valid(self):
        self.assertEqual(main_with_args(7, [
            [4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [4, -1, -1], [7, -1, -1]
        ]), "CORRECT")


if __name__ == '__main__':
    unittest.main()
