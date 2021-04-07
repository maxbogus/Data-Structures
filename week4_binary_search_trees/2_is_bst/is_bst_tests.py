import unittest

from is_bst import main_with_args


class MyTestCase(unittest.TestCase):
    def test_sample_one(self):
        self.assertEqual(main_with_args(3, [[2, 1, 2], [1, - 1, - 1], [3, - 1, - 1]]), "CORRECT")

    def test_sample_one_second(self):
        self.assertEqual(main_with_args(3, [[2, 1, 2], [2, - 1, - 1], [1, - 1, - 1]]), "INCORRECT")

    def test_sample_two(self):
        self.assertEqual(main_with_args(3, [[1, 1, 2], [2, -1, -1], [3, -1, -1]]), "INCORRECT")

    def test_sample_three(self):
        self.assertEqual(main_with_args(0), "CORRECT")

    def test_sample_four(self):
        self.assertEqual(main_with_args(5, [
            [1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]), "CORRECT")

    def test_sample_four_second(self):
        self.assertEqual(main_with_args(5, [
            [1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [0, -1, -1]]), "INCORRECT")

    def test_sample_four_third(self):
        self.assertEqual(main_with_args(5, [
            [6, 1, -1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]), "CORRECT")

    def test_sample_five(self):
        self.assertEqual(main_with_args(7, [
            [4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]
        ]), "CORRECT")

    def test_sample_six(self):
        self.assertEqual(main_with_args(4, [
            [4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]]), "INCORRECT")

    def test_sample_five_second(self):
        self.assertEqual(main_with_args(7, [
            [4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [7, -1, -1], [5, -1, -1]
        ]), "INCORRECT")

    def test_sample_eight(self):
        self.assertEqual(main_with_args(3, [
            [2, 1, 2], [1, -1, -1], [2, -1, -1]
        ]), "CORRECT")

    def test_sample_seven(self):
        self.assertEqual(main_with_args(3, [
            [2, 1, 2], [2, -1, -1], [3, -1, -1]
        ]), "CORRECT")

    def test_sample_six_second(self):
        self.assertEqual(main_with_args(1, [2147483647, -1, -1]), "CORRECT")

    def test_two_scenario(self):
        self.assertEqual(main_with_args(3, [[2, 1, 2], [1, - 1, - 1], [2147483647, - 1, - 1]]), "CORRECT")


if __name__ == '__main__':
    unittest.main()
