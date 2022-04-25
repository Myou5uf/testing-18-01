



def solve(countIp,ipAdress):
    try:
       ipAddress = validateIp(countIp,ipAdress)
       mask = [i for i in "255.255.255.248".split('.')]
       mask_bin = bin(int(mask[-1])).split('b')[-1]
       print(mask_bin)
       result = []
       for index,address in enumerate(ipAddress,0):
            binNumber = str(bin(int(address[-1])).split('b')[-1])
            if (len(binNumber) != 8) :
                while len(binNumber) < 8:
                   binNumber = '0'+binNumber
            result.append(binToDec(logicAnd(mask_bin,binNumber)))

       ip = '.'.join([i for i in ipAddress[-1][0:-1]])+'.'+str(min(result))
       mask = '.'.join([i for i in mask])
       return (ip,mask)    
    except(AttributeError):
        print('Error')

def logicAnd(first,second):
    result = ''
    for i in range(len(first)):
        if (int(first[i]) == 1 and int(second[i]) == 1):
            result +='1'
        else:
            result +='0'
    return result

def  binToDec(digit):
    digitLen = len(digit)
    digitDec = 0
    for i in range(digitLen):
        digitDec = digitDec + int(digit[i]) * (2**(digitLen-i-1))
    return digitDec

    
def validateIp(countIp,array):
    if (type(countIp) == str):
        raise TypeError("Валидация не прошла")
    elif ((countIp == 0 or len(array) == 0) or (countIp>=1000 or len(array) >= 1000)):
        raise ValueError("Валидация не прошла")
    elif (countIp == len(array)):
        ipAddress = [ array[i].split('.') for i in range(len(array))]
        for i in ipAddress:
            if (len(i) == 4):
                for j in i:
                    if (int(j)):
                        continue
                continue
            else:
                raise ValueError("Валидация не прошла")
        return ipAddress
    else:
        raise ValueError("Валидация не прошла")
    
    


# print(solve('2', ['212.65.71.73', '212.65.71.79', '212.65.71.74']))
print(solve(3, ['212.65.71.73', '212.65.71.79', '212.65.71.74']))
# print(validateIp(4, [212,65,71,73]))
