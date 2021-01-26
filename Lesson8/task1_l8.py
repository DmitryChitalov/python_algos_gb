"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
"""

# Прошу простить, что не смотря на предупреждение, решение мною взято из примера.
# я весьма долго пыталась разобраться в алгоритме вообще, и решение через коллекции
# стало более-менее мне понятно
# Хаффман через коллекции

from collections import Counter, deque

def haffman_tree(s):
    count = Counter(s)   #подсчет уникальных символов
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1])) #сортировка по возрастанию числа повторений
    if len(sorted_elements) != 1:     #проверка на единственный повтояющийся символ
        while len(sorted_elements) > 1:    #собственно постройка дерева
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            for i, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elements.insert(i, (comb, weight))
                    break
            else:
                sorted_elements.append((comb, weight))
    else:
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    return sorted_elements[0][0]

code_table = dict()   #кодовая таблица!!

def haffman_code(tree, path=''):
    if not isinstance(tree, dict):  # Если элемент не словарь, заносим его, а так же его код в словарь (кодовую таблицу).
        code_table[tree] = path
    else:                           # Если элемент словарь, рекурсивно спускаемся вниз
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')

s = "wibbly wobbly timey wimey"

haffman_code(haffman_tree(s))
for i in s:
    print(code_table[i], end=' ')
print()

# ОДНО ИЗ РЕШЕНИЙ ИЗ ДЕДЛАЙНА
"""Хаффман через ООП"""

string = "beep boop beer!"
print("Исходная строка: " + string)


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def make_haffman_tree(node, code=""):
    if type(node) is str:
        return {
            node: code
        }

    l, r = node.children()

    result = {}
    # 0 - налево, 1 - направо
    result.update(make_haffman_tree(l, code + "0"))
    result.update(make_haffman_tree(r, code + "1"))

    return result


frequencies = {}
for char in string:
    if char not in frequencies:
        frequencies[char] = 0

    frequencies[char] += 1

tree = frequencies.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append(
        (Node(char1, char2), count1 + count2)
    )

code_table = make_haffman_tree(tree[0][0])

coded = []
for char in string:
    coded.append(code_table[char])

print("Закодированная строка: %s" % "".join(coded))

