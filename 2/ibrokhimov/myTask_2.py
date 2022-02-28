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
    dict = {}
    for i in range(len(data)):
        if data[i] in dict.keys():
            dict[data[i]] += 1
        else:
            dict.update({data[i]: 1})

    print(dict)
    if 5 in dict.values():
        print("poker")
    elif 4 in dict.values():
        print("four if a kind")
    elif 3 in dict.values() and 2 in dict.values():
        print("full house")
    elif 3 in dict.values():
        print("three of kind")
    elif 2 in dict.values() and len(dict) == 3:
        print("two pairs")
    elif 2 in dict.values():
        print("one pairs")
    else:
        print("all different")


inputData = list(
    map(int, input("Введите 5 целых положительных чисел, не превосходящих 10^9 через пробел: ").split(" ")))
countIdenticalCard(inputData)

