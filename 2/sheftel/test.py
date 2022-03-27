import unittest
import task


class MyTestCase(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(task.solve(8, ['BAY', 'PET', 'RAY', 'BET', 'ONE', 'TWO', 'BAT', 'RAT']), (4, ['BAY', 'BAT', 'BET', 'PET']))

    def test_negative(self):
        self.assertEqual(task.solve(5, ['AA', 'BB', 'AC', 'CB', 'ZZ']), 0)

    def test_type_mismatch_1(self):
        self.assertRaises(TypeError, task.solve, ('Word', ['11', 'aa']))

    def test_type_mismatch_2(self):
        self.assertRaises(TypeError, task.solve, 12, 8)

    def test_index_mismatch_1(self):
        self.assertRaises(ValueError, task.solve, -5, [])

    def test_index_mismatch_2(self):
        self.assertRaises(ValueError, task.solve, 3, [])


if __name__ == '__main__':
    unittest.main()
