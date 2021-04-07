import unittest
from max_sliding_window import max_sliding_window_naive, max_sliding_window_optimal

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(max_sliding_window_optimal('2 7 3 1 5 2 6 2', 4), [7, 7, 5, 6, 6])


if __name__ == '__main__':
    unittest.main()
