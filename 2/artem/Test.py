import unittest
import Testing


class dataTest(unittest.TestCase):
    def test_pastToFuture(self):
        self.assertEqual(Testing.calc('2-(7+3*4)/5'),-1)  # add assertion here
    def test_futureToFuture(self):
        self.assertEqual(Testing.calc('1/(1-1)'),'Error')

if __name__ == '__main__':
    unittest.main()
