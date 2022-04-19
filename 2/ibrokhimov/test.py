import unittest
import myTask_2


class MyTestCase(unittest.TestCase):
    def test_valError(self):
      self.assertRaises(ValueError, myTask_2.countIdenticalCard, "0.75 2 3 45 6")

    def test_valErrorStr(self):
      self.assertRaises(ValueError, myTask_2.countIdenticalCard, "test")

    def test_typeErrorInt(self):
        self.assertRaises(TypeError, myTask_2.countIdenticalCard, 2, 1, 2, 2, 3)

    def test_attributeError(self):
        self.assertRaises(AttributeError, myTask_2.countIdenticalCard, 1)
if __name__ == '__main__':
    unittest.main()
