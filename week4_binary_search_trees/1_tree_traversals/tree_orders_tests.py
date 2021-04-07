import unittest

from tree_orders import TreeOrders


class MyTestCase(unittest.TestCase):
    first_tree_orders = TreeOrders()
    first_tree_orders.read_from_array(5, [
        [4, 1, 2],
        [2, 3, 4],
        [5, -1, -1],
        [1, -1, -1],
        [3, -1, -1]
    ])
    second_tree_orders = TreeOrders()
    second_tree_orders.read_from_array(10, [
            [0, 7, 2],
            [10, -1, -1],
            [20, -1, 6],
            [30, 8, 9],
            [40, 3, -1],
            [50, -1, -1],
            [60, 1, -1],
            [70, 5, 4],
            [80, -1, -1],
            [90, -1, -1]
        ])

    def test_first_case_in_order(self):
        self.assertEqual(self.first_tree_orders.in_order(), [1, 2, 3, 4, 5])

    def test_first_case_post_order(self):
        self.assertEqual(self.first_tree_orders.pre_order(), [4, 2, 1, 3, 5])

    def test_first_case_pre_order(self):
        self.assertEqual(self.first_tree_orders.post_order(), [1, 3, 2, 5, 4])

    def test_second_case_in_order(self):
        self.assertEqual(self.second_tree_orders.in_order(), [50, 70, 80, 30, 90, 40, 0, 20, 10, 60])

    def test_second_case_post_order(self):
        self.assertEqual(self.second_tree_orders.pre_order(), [0, 70, 50, 40, 30, 80, 90, 20, 60, 10])

    def test_second_case_pre_order(self):
        self.assertEqual(self.second_tree_orders.post_order(), [50, 80, 90, 30, 40, 70, 10, 60, 20, 0])


if __name__ == '__main__':
    unittest.main()
