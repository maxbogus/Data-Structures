import unittest
from check_brackets import find_mismatch
from itertools import combinations, product


class MyTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(find_mismatch('[]'), 'Success')
        self.assertEqual(find_mismatch('[]{}'), 'Success')
        self.assertEqual(find_mismatch('[{}]'), 'Success')
        self.assertEqual(find_mismatch('(())'), 'Success')
        self.assertEqual(find_mismatch('{[]}()'), 'Success')

    def test_fail(self):
        self.assertEqual(find_mismatch('{'), 1)
        self.assertEqual(find_mismatch('}'), 1)
        self.assertEqual(find_mismatch('{[}'), 3)
        self.assertEqual(find_mismatch('foo(bar[i);'), 10)
        self.assertEqual(find_mismatch('[]({)'), 5)
        self.assertEqual(find_mismatch('[{}]{'), 5)

    def test_one(self):
        def count():
            result = 0
            for i in range(1000):
                if i % 2 == 0 or i % 3 == 0:
                    result += 1
            return result
        self.assertEqual(count(), 667)

    def test_two(self):
        def count():
            result = 0
            for i in range(1, 9999):
                substring = '{}'.format(i)
                if substring.count('1') == 1 and substring.count('3') == 1:
                    result +=1
            return result
        self.assertEqual(count(), 333)

    def test_three(self):
        def count():
            n = 100
            counter = 0

            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        # if i < j < k:
                        counter += 1

            return counter
        self.assertEqual(count(), 6)

    def test_four(self):
        count = 0
        for d in product(range(10), repeat=6):
            print(d.count(0), d.count(1))
            if d.count(0) == d.count(1):
                count += 1
        self.assertEqual(count, 36)


if __name__ == '__main__':
    unittest.main()
