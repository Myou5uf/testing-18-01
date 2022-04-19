import unittest
import task


class MyTestCase(unittest.TestCase):

    def test_works_1(self):
        self.assertEqual(task.run, [[3, 10], [7, 11], [4, 6], [5, 8]], 15)

    def test_works_2(self):
        self.assertEqual(task.run, [[3, 10], [11, 20], [13, 14], [20, 21]], 10)

    def test_data_mismatch_1(self):
        self.assertRaises(ValueError, task.run, [[2, 10], [7, 11], [4, 6], [5, 8]])

    def test_data_mismatch_2(self):
        self.assertRaises(ValueError, task.run, [[3, 10], [7], [4, 6], [5, 8]])

    def test_type_mismatch_1(self):
        self.assertRaises(TypeError, task.run, [['3', 10], [7, 11], [4, 6], [5, 8]])

    def test_borders_1(self):
        self.assertRaises(ValueError, task.run, [[0, 10], [11, 20], [13, 14], [20, 21]])

    def test_borders_2(self):
        self.assertRaises(ValueError, task.run, [[3, 0], [11, 20], [13, 14], [20, 21]])

    def test_borders_4(self):
        self.assertRaises(ValueError, task.run, [[3, 10**10], [11, 20], [13, 14], [20, 21]])

    def test_borders_5(self):
        self.assertRaises(ValueError, task.run, [[3, 10], [0, 20], [13, 14], [20, 21]])

    def test_borders_6(self):
        self.assertRaises(ValueError, task.run, [[3, 10], [17, 11], [13, 14], [20, 21]])

    def test_borders_7(self):
        self.assertRaises(ValueError, task.run, [[3, 10], [10**7, 10**8], [13, 14], [20, 21]])


if __name__ == '__main__':
    unittest.main()
