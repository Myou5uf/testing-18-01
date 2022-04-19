import unittest
import task


class MyTestCase(unittest.TestCase):
    def test_nameError(self):
        self.assertRaises(ValueError, task.lazy, 2, ['1.5 2', '2 3'])

    def test_typeErrorStr(self):
        self.assertRaises(TypeError, task.lazy, '1', ['1 2', '2 3'])

    def test_typeErrorInt(self):
        self.assertRaises(TypeError, task.lazy, 2, 1, 2, 2, 3)

    def test_attributeError(self):
        self.assertRaises(AttributeError, task.lazy, 1, [1, 2, 2, 3])

    def test_minCountN(self):
        self.assertRaises(IndexError, task.lazy, 0, ['1 2', '2 3'])

    def test_maxCountN(self):
        self.assertRaises(IndexError, task.lazy, 101, ['1 2', '2 3'])

    def test_minCountA(self):
        self.assertRaises(IndexError, task.lazy, 2, ['0 1', '1 2'])

    def test_maxCountA(self):
        self.assertRaises(IndexError, task.lazy, 2, ['1 29', '32 33'])


if __name__ == '__main__':
    unittest.main()
