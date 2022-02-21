import unittest
import task


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(task.lazy(2, ['1 2', '3 4']), 'NO')  # add assertion here


if __name__ == '__main__':
    unittest.main()
