import unittest
import Van


class dataTest(unittest.TestCase):
    def test_pastToFuture(self):
        self.assertEqual(Van.calc('2016-02-16','2022-03-01'),'2205')  # add assertion here
    def test_futureToFuture(self):
        self.assertEqual(Van.calc('2096-03-01','2051-02-16'),'16450')

if __name__ == '__main__':
    unittest.main()
