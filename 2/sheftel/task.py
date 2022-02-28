# В известной игре(также называемой "Метаграммой") необходимо из одного слова сделать другое, меняя за один ход по
# одной букве. Например, сделать из мухи слона можно так: муха - мура - тура - тара - кара - каре - кафе - кафр -
# каюр - каюк - крюк - урюк - урок - срок - сток - стон - слон. Напишите программу, которая по данному набору слов,
# начальному и конечному слову, находит самый короткий способ превратить одно слово в другое. Формат входных данных:
# Первое число входных данных содержит целое число N, 2≤N≤105. Далее идет N различных строчек, каждая из которых
# содержит одно словарное слово. Все слова состоят из заглавных латинских букв  и имеют равную длину,
# не превосходящую 10. Программа должна найти наименьшую цепочку, состоящую из данных слов. Цепочка должна начинаться
# со слова, идущего в словаре первым и заканчиваться словом, идущим в словаре вторым. Два соседних слова в цепочке
# должны отличаться ровно в одной букве. Формат выходных данных: Первая строка выходных данных должна содержать
# количество слов в минимальной искомой цепочке(включая начальное и конечное слово). Далее должны идти все слова
# цепочки. Если искомой цепочки не существует, программа должна вывести число 0.
# Пример
# Вход: 8 BAY PET RAY BET ONE TWO BAT RAT
# Выход: 4 BAY BAT BET PET
# Вход: 5 AA BB AC CB ZZ
# Выход: 0



"""def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList = set(wordList)
    if endWord not in wordList:
        return 0
    que = [beginWord]
    j = 0
    while que:
        j = j + 1
        l = len(que)
        while l:
            curr = que[0]
            del que[0]
            for i in range(len(curr)):
                for k in range(ord("a"), ord("z") + 1):
                    new_word = curr[:i] + chr(k) + curr[i + 1:]
                    if new_word == endWord:
                        return j + 1
                    if new_word in wordList:
                        que.append(new_word)
                        wordList.remove(new_word)
            l = l - 1
    return 0"""


def solve(n, words):
    que = [words[0]]
    line = [words[0]]
    target = words[1]
    words = set(words)
    j = 0
    while que:
        j = j + 1
        l = len(que)
        while l:
            curr = que[0]
            del que[0]
            for i in range(len(curr)):
                for k in range(ord("A"), ord("Z") + 1):
                    new_word = curr[:i] + chr(k) + curr[i + 1:]
                    if new_word == target:
                        line.append(new_word)
                        return j + 1, line
                    if new_word in words:
                        que.append(new_word)
                        line.append(new_word)
                        words.remove(new_word)
            l = l - 1
    return 0


def task():
    n = int(input())
    words = [i for i in input().split(' ')]

    print(solve(n, words))


if __name__ == '__main__':
    task()

