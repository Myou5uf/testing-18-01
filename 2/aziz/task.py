


def solve(countIp,ipAdress):
    try:
        if ((countIp == 0 or len(ipAdress) == 0) or (countIp>=1000 or len(ipAdress) >= 1000)):
           raise ValueError("Ошибка")
        elif (countIp==len(ipAdress)):
            mask = "255.255.255.248"
            result = []
            for i in range(countIp):
                for j in ipAdress:
                    if type(j) != str:
                        raise TypeError("Ошибка")
                    else:
                        value = j.split(' ')
                        
        else:
            raise ValueError("Ошибка")
    except(ValueError, TypeError):
        print('Error')


    



print(solve('2', ['212.65.71.73', '212.65.71.79', '212.65.71.74']))
print(solve('2', ['212.65.71.73', '212.65.71.79', '212.65.71.74']))