import unittest
import task


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(task.lazy(2, ['1 2', '3 4']), 'NO')  # add assertion here\

    def test_positive(self):
        self.assertEqual(task.lazy(3, ['1 2', '2 3', '2 4']), 'YES')

    def test_positive(self):
        self.assertEqual(task.lazy(5, ['1 2', '2 3', '4 5', '1 5', '29 30']), 'NO')

    def test_positive(self):
        self.assertEqual(task.lazy(4, ['5 7', '1 5', '3 5', '5 8']), 'YES')


if __name__ == '__main__':
    unittest.main()
