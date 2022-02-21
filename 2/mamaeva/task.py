def lazy(n, shedule):
  days = []
  for i in range(31):
    days.append(0)
  for i in range(n):
    day = shedule[i].split(' ')
    startday = int(day[0])
    endday = int(day[1])
    for j in range(startday, endday + 1):
      days[j - 1] = days[j - 1] + 1
  if n in days:
    return 'YES'
  else:
    return 'NO'
