import unittest

from phone_book import write_responses, read_queries, process_queries, Query


class MyTestCase(unittest.TestCase):
    def test_full(self):
        input = [
            'add 911 police',
            'add 76213 Mom',
            'add 17239 Bob',
            'find 76213',
            'find 910',
            'find 911',
            'del 910',
            'del 911',
            'find 911',
            'find 76213',
            'add 76213 daddy',
            'find 76213'
        ]
        tests = []
        for i in range(len(input)):
            tests.append(Query(input[i].split()))
        self.assertEqual(process_queries(tests), ['Mom',
                                                                   'not found',
                                                                   'police',
                                                                   'not found',
                                                                   'Mom',
                                                                   'daddy', ])


if __name__ == '__main__':
    unittest.main()
