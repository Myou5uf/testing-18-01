# В музее регистрируется в течение дня время прихода и ухода каждого посетителя.
# Таким образом за день получены N пар значений,
# где первое значение в паре показывает время прихода посетителя и второе значения - время его ухода.
# Найти промежуток времени, в течение которого в музее одновременно находилось максимальное число посетителей.
# Пример:
# n =3
# 12:33,14:45
# 13:12,17:56
# 11:46,13:01
# solve(4,[['8:46','12:41'],['11:33','14:45'],['12:12','15:56'],['9:42','10:12']])
from datetime import time, datetime


def solve(n, entries):
    if not isinstance(n, int):
        raise TypeError("Value must be integer")
    if not isinstance(entries, list):
        raise TypeError("Value must be list")
    if n < 1 or n > 100:
        raise ValueError("Value out of allowed range")
    if len(entries) != n:
        raise ValueError("Number of elements in list not consistent with given number")
    max_number = {
        'value': 0,
        'start_time': None,
        'end_time': None,
    }
    number = 0
    starts = []
    ends = []
    timetable = []
    for entry in entries:
        x_0 = datetime.strptime(entry[0], '%H:%M').time()
        x_1 = datetime.strptime(entry[1], '%H:%M').time()
        starts.append(x_0)
        ends.append(x_1)
        timetable.append(x_0)
        timetable.append(x_1)
    timetable.sort()
    starts.sort()
    ends.sort()
    for time in timetable:
        if not (time in starts and time in ends):
            if time in starts:
                number += 1
                if number >= max_number['value']:
                    max_number['value'] = number
                    max_number['start_time'] = time
            if time in ends:
                if number == max_number['value']:
                    max_number['end_time'] = time
                number -= 1
    return max_number


def run():
    n = int(input())
    entries = []
    for i in range(0, n):
        x = input().split(',')
        entries.append([x[0].strip(), x[1].strip()])
    print(solve(n, entries))


if __name__ == '__main__':
    run()
