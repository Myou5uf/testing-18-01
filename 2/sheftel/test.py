import unittest
import task


class MyTestCase(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(task.solve(8, ['BAY', 'PET', 'RAY', 'BET', 'ONE', 'TWO', 'BAT', 'RAT']), (4, ['BAY', 'BAT', 'BET', 'PET']))

    def test_negative(self):
        self.assertEqual(task.solve(5, ['AA', 'BB', 'AC', 'CB', 'ZZ']), (0, []))

    def test_empty_mismatch_1(self):
        self.assertIsInstance(task.solve(0, ['11', 'aa']), str)

    def test_input_mismatch_2(self):
        self.assertIsInstance(task.solve(12, []), str)

    def test_input_negative(self):
        self.assertIsInstance(task.solve(-5, []), str)


if __name__ == '__main__':
    unittest.main()
