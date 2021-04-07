import unittest

from hash_chains import QueryProcessor, read_querie_with_arg


class MyTestCase(unittest.TestCase):
    def test_check(self):
        query_proc = QueryProcessor(1)
        data = read_querie_with_arg('check 0')
        self.assertEqual(query_proc.process_query(data), query_proc.process_query_naive(data))

    def test_find(self):
        query_proc = QueryProcessor(1)
        data = read_querie_with_arg('find 0')
        self.assertEqual(query_proc.process_query(data), query_proc.process_query_naive(data))

    def test_add(self):
        query_proc = QueryProcessor(1)
        data = read_querie_with_arg('add 0')
        self.assertEqual(query_proc.process_query(data), query_proc.process_query_naive(data))

    def test_del(self):
        query_proc = QueryProcessor(1)
        data = read_querie_with_arg('del 0')
        self.assertEqual(query_proc.process_query(data), query_proc.process_query_naive(data))


if __name__ == '__main__':
    unittest.main()
