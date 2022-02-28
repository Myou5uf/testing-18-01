# Покер.
# Известное казино хочет поправить свое пошатнувшееся финансовое положение, установив новую модель игровых
# автоматов "Покер" улучшенного дизайна. Игроку в покер необходимо собрать 5 карт таким образом, чтобы среди них
# было максимальное количество совпадающих (лучшая комбинация – все пять карт совпадает, а худшая – все различны).
# К сожалению, главный программист казино недавно неожиданно разбогател, уволился и уехал на Багамы.
# Без него казино не может решить, как по выпавшему набору карт определить размер выигрыша клиента.
# Помогите казино справиться с этой задачей.

# Input: 7 3 7 7 3 Output: full house
# Input: 4 1 4 9 4 Output: three of kind
# Input: 7 45 12 267 7 Output: one pair

def countIdenticalCard(data):
    count = 0
    k = 0
    for i in range(len(data)):
        k = 0
        for j in range(len(data)):
            if data[j] == data[i]:
                k += 1
        count += k

    return count


inputData = list(
    map(int, input("Введите 5 целых положительных чисел, не превосходящих 10^9 через пробел: ").split(" ")))
result = countIdenticalCard(inputData)
print(result)

if result == 25:
    print("poker")
elif result == 17:
    print("four if a kind")
elif result == 13:
    print("full house")
elif result == 11:
    print("three of kind")
elif result == 9:
    print("two pairs")
elif result == 7:
    print("one pair")
else:
    print("all different")
