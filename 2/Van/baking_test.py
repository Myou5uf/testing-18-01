import unittest
import banking


class dataTest(unittest.TestCase):
    def test_pastToFuture(self):
        self.assertEqual(banking.change(40, [1, 3, 7, 12, 32]), '1 7 32')  # add assertion here
    def test_futureToFuture(self):
        self.assertEqual(banking.change(99, [10, 50, 100, 500, 1000]), "impossible")


if __name__ == '__main__':
    unittest.main()