import unittest
from job_queue import assign_jobs, assign_jobs_fast


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(assign_jobs(2, [2]), assign_jobs_fast(2, [2]))


if __name__ == '__main__':
    unittest.main()
