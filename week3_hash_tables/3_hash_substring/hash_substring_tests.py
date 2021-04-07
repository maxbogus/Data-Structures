import unittest
from hash_substring import get_occurrences, get_occurrences_naive


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_occurrences('a', 'abc'), get_occurrences_naive('a', 'abc'))

    def test_something_1(self):
        self.assertEqual(get_occurrences('c', 'abc'), get_occurrences_naive('c', 'abc'))

    def test_something_2(self):
        self.assertEqual(get_occurrences('a', 'aaa'), get_occurrences_naive('a', 'aaa'))

    def test_something_3(self):
        self.assertEqual(get_occurrences('z', 'cat'), get_occurrences_naive('z', 'cat'))


if __name__ == '__main__':
    unittest.main()
