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


class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def shortest_path(self, target):
        path_list = [[self]]
        path_index = 0
        # To keep track of previously visited nodes
        previous_nodes = {self}
        if self == target:
            return path_list[0]

        while path_index < len(path_list):
            current_path = path_list[path_index]
            last_node = current_path[-1]
            next_nodes = last_node.children

            for next_node in next_nodes:
                if next_node.data == target.data:
                    current_path.append(target)
                    return current_path
                if next_node not in previous_nodes:
                    new_path = current_path[:]
                    new_path.append(next_node)
                    path_list.append(new_path)
                    previous_nodes.add(next_node)
            path_index += 1
        return []


def solve(n, words):
    if not isinstance(n, int):
        raise TypeError("Value must be integer")
    if not isinstance(words, list):
        raise TypeError("Value must be list")
    if n < 2 or n > 105:
        raise ValueError("Value out of allowed range")
    if len(words) != n:
        raise ValueError("Number of elements in list not consistent with given number")
    for word in words:
        if not isinstance(word, str):
            raise TypeError("All values in list must be string")
        for letter in word:
            if letter.islower():
                raise ValueError("All letters must be uppercase")
    start = Tree(words[0])
    target = Tree(words[1])
    words = words[1:]
    queue = [start]
    while queue:
        while len(queue):
            word_children(queue[0], words)
            queue.extend(queue[0].children)
            del queue[0]
    path = start.shortest_path(target)
    if len(path):
        for i in range(len(path)):
            path[i] = path[i].data
        return len(path), path
    return len(path)


def word_children(parent, words):
    for i in range(len(parent.data)):
        for k in range(ord("A"), ord("Z") + 1):
            new_word = parent.data[:i] + chr(k) + parent.data[i + 1:]
            if new_word in words:
                words.remove(new_word)
                parent.children.append(Tree(new_word))


def task():
    n = int(input())
    words = [i for i in input().split(' ')]

    print(solve(n, words))


if __name__ == '__main__':
    task()
