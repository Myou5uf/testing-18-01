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

CLOCK = True
COUNTER = False
UNDEFINED = None


def get_counter_spin(spin1: bool, spin2: bool):
    if spin2 == UNDEFINED:
        return not spin1
    if spin1 == CLOCK and spin2 == COUNTER:
        return COUNTER
    if spin1 == COUNTER and spin2 == CLOCK:
        return CLOCK
    return UNDEFINED


def solve(gear_count: int, connections):
    result = [UNDEFINED if i > 0 else CLOCK for i in range(0, gear_count)]
    for gear1, gear2 in connections:
        i, j = gear1 - 1, gear2 - 1
        if result[i] != UNDEFINED:
            result[j] = get_counter_spin(result[i], result[j])
        if result[j] != UNDEFINED:
            result[i] = get_counter_spin(result[j], result[i])
        if result[i] == UNDEFINED or result[j] == UNDEFINED:
            return []
    return ['clockwise' if x else 'counter-clockwise' for x in result ]


def main():
    n = int(input())
    m = int(input())
    connections = []
    for _ in range(0, m):
        x = input().split(' ')
        if 1 <= int(x[0]) <=n and 1 <= int(x[1]) <= n:
            connections.append([int(x[0]), int(x[1])])
    result = solve(n, connections)
    for r in result:
        print(r)


if __name__ == '__main__':
    main()