import unittest
from Van import banking


class MyTestCase(unittest.TestCase):
    def test_work(self):
        self.assertEqual(banking.change(40, [1, 3, 7, 12, 32]), '1 7 32')

    def test_impossible(self):
        self.assertEqual(banking.change(99, [10, 50, 100, 500, 1000]),'impossible')

    def test_type_mismatch(self):
        self.assertEqual(banking.change(0,[]))
        
    def test_type_mismatch_1(self):
        self.assertRaises(TypeError,banking.change('10',[10,300,30,20,90]))

    def test_type_mismatch_2(self):
        self.assertRaises(TypeError,banking.change(10,['10',300,30,20,90]))
     

if __name__ == '__main__':
    unittest.main()