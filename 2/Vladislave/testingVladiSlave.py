import unittest
import Van


class dataTest(unittest.TestCase):
    def test_pastToFuture(self):
        self.assertEqual(Van.calc('2016-02-16','2022-03-01'),'2205')  # add assertion here
    def test_futureToFuture(self):
        self.assertEqual(Van.calc('3000-03-01','0001-02-16'),'1095375')
    def test_moreYear(self):
        self.assertEqual(Van.calc('',''),None)
    def test_looongYear(self):
        self.assertEqual(Van.calc('0001-12-22','3000000000000-10-01'),'Error_in_second_date')

if __name__ == '__main__':
    unittest.main()
