import unittest
from tree_height_lib import TreeHeight

class MyTestCase(unittest.TestCase):
    def test_something(self):
        tree = TreeHeight([4, -1, 4, 1, 1], 5)
        self.assertEqual(tree.compute_height_fast(), tree.compute_height())


if __name__ == '__main__':
    unittest.main()
