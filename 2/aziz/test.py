import unittest
import task

class MyTestCase(unittest.TestCase):

    def test_works(self):
        self.assertEqual(task.solve(3, ['212.65.71.73', '212.65.71.79', '212.65.71.74']), ('212.65.71.72', '255.255.255.248'))

    def test_data_mismatch(self):
        self.assertRaises(ValueError, task.solve(2, ['212.65.71.73', '212.65.71.79', '212.65.71.74']))

    def test_type_mismatch_1(self):
        self.assertRaises(TypeError, task.solve('2', ['212.65.71.73', '212.65.71.79', '212.65.71.74']))

    def test_type_mismatch_2(self):
        self.assertRaises(TypeError, task.solve(3, [212, 79, 212]))

    def test_type_mismatch_3(self):
        self.assertRaises(TypeError, task.solve(3, ['212.65.71.73', '212.65.71.79', 212]))

    def test_borders_1(self):
        self.assertRaises(ValueError, task.solve,0, [])

    def test_borders_2(self):
        strings = ['212.65.71.' + str(randint(73,79)) for i in range(0,1000) ]
        self.assertRaises(ValueError, task.solve, 1000, strings)


if __name__ == '__main__':
    unittest.main()