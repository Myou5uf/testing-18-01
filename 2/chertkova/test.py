import unittest
import task


class MyTestCase(unittest.TestCase):

    def test_success(self):
        self.assertEqual(task.run(180), 36)

    def test_failure(self):
        self.assertEqual(task.run(179), 'impossible')

    def test_type_mismatch_1(self):
        self.assertRaises(TypeError, task.run('2'))

    def test_borders_1(self):
        self.assertRaises(ValueError, task.run, 0)

    def test_borders_2(self):
        self.assertRaises(ValueError, task.run, 2*10**9+1)


if __name__ == '__main__':
    unittest.main()
