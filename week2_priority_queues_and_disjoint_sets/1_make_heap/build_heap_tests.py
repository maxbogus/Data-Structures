import unittest
from build_heap import build_heap_fast, build_heap, main
from heapq import heapify
from itertools import permutations
import itertools as it


class MyTestCase(unittest.TestCase):
    def test_that_heap_is_valid(self):
        data = [3, 2, 4, 0, 1]
        heapify(data)
        self.assertEqual(data, build_heap_fast([3, 2, 4, 0, 1]))

    def test_that_heap_is_valid_two(self):
        data = [0, 1]
        heapify(data)
        self.assertEqual(data, build_heap_fast([0, 1]))
        self.assertEqual(data, build_heap_fast([1, 0]))

    def test_that_heap_is_valid_three(self):
        data = [3, 2, 0, 1]
        heapify(data)
        self.assertEqual(data, build_heap_fast([3, 2, 0, 1]))

    def test_list_of_changes_is_valid(self):
        self.assertEqual(build_heap([0, 1]), build_heap_fast([0, 1]))

    def test_all(self):
        counter = 0

        for d in it.product(range(10), repeat = 4):
            if sum(d) == 10:
                print(d)
                counter += 1
        print(counter)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
