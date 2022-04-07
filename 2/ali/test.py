import unittest
import task


class MyTestCase(unittest.TestCase):

    def test_works_1(self):
        self.assertEqual(task.solve(4, [['8:46', '12:41'], ['11:33', '14:45'], ['12:12', '15:56'], ['9:42', '10:12']]),
                         (3, '12:12', '12:41'))

    def test_works_2(self):
        self.assertEqual(task.solve(1, ['12:00', '18:00']), (1, '12:12', '12:41'))

    def test_data_mismatch_1(self):
        self.assertRaises(ValueError, task.solve(2, [['8:46', '12:41'], ['11:33', '14:45'], ['12:12', '15:56']]))

    def test_data_mismatch_2(self):
        self.assertRaises(ValueError, task.solve(3, [['8:46'], ['11:33', '14:45'], ['12:12', '15:56']]))

    def test_type_mismatch_1(self):
        self.assertRaises(TypeError, task.solve('3', [['8:46', '12:41'], ['11:33', '14:45'], ['12:12', '15:56']]))

    def test_type_mismatch_2(self):
        self.assertRaises(TypeError, task.solve(3, [[8, 41], ['11:33', 14], ['12:12', '15:56']]))

    def test_type_mismatch_3(self):
        self.assertRaises(TypeError, task.solve(3, ['212.65.71.73', '212.65.71.79', 212]))

    def test_borders_1(self):
        self.assertRaises(ValueError, task.solve, 0, [])

    def test_borders_2(self):
        self.assertRaises(ValueError, task.solve, 1000, [['8:46', '12:41'], ['11:33', '14:45'], ['12:12', '15:56']])


if __name__ == '__main__':
    unittest.main()
