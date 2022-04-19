# ШЕСТЕРЕНКИ
# На плоскости расположена система из N одинаковых шестеренок, 
# которая приводится в движение вращением шестеренки 1 по часовой стрелке (`clockwise'). 
# Требуется определить направление вращения каждой шестеренки системы, либо установить, что систему заклинит.

# Входные данные
# Первая строка входных данных содержит число шестеренок N, 1<N≤1000.

# Вторая строка содержит число M. Далее идет M строк, каждая из которых содержит два различных числа i и j, 
# означающих, что шестеренки с номерами i и j сцеплены. 
# При этом каждая шестеренка сцеплена не более, чем с 6 другими шестеренками. 
# Также гарантируется, что все шестеренки соединены с первой через несколько других шестеренок 
# (то есть в незаклиненной системе будут вращаться все шестеренки).

# Выходные данные
# Программа должна вывести на экран N строк. Строка с номером i должна содержать слово `clockwise', 
# если шестеренка i вращается по часовой стрелке или слова `counter-clockwise' в противном случае. 
# Если систему заклинит, то программа не должна выводить ничего.

# Пример входных данных
# 5
# 5
# 1 2
# 2 3
# 5 3
# 2 4
# 4 5
# Пример выходных данных
# clockwise
# counter-clockwise
# clockwise
# clockwise
# counter-clockwise

import unittest
from program import solve


CLOCK = 'clockwise'
COUNTER = 'counter-clockwise'

class TestCheriaev(unittest.TestCase):

    def test_works_1(self):
        self.assertEqual(
            [
                CLOCK,
                COUNTER,
                CLOCK,
                CLOCK,
                COUNTER
            ],
            solve(5, [[1, 2], [2, 3], [5, 3], [2, 4], [4, 5]])
        )

    def test_works_2(self):
        self.assertEqual(
            [
                CLOCK,
                COUNTER,
                CLOCK,
                CLOCK,
                COUNTER,
                COUNTER,
                COUNTER
            ],
            solve(7, [[1, 2], [2, 3], [5, 3], [4, 5], [6, 4], [6, 1], [7, 1]])
        )

    def test_jammed_1(self):
        self.assertEqual(
            [],
            solve(3, [[1, 2], [2, 3], [3, 1]])
        )

    def test_jammed_2(self):
        self.assertEqual(
            [],
            solve(7, [[1, 2], [2, 3], [5, 3], [4, 5], [6, 4], [6, 1], [7, 6], [7, 1]])
        )

    def test_jammed_if_both_spins_are_undefined(self):
        self.assertEqual(
            [],
            solve(3, [[2, 3], [1, 2]])
        )


if __name__ == '__main__':
    unittest.main()