"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
from collections import deque, Counter

result = dict()


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def tree(s):
    counting = Counter(s)
    sorting = deque(sorted(counting.items(), key=lambda item: item[1]))
    while len(sorting) > 1:
        weight = sorting[0][1] + sorting[1][1]
        leaf = Node(left=sorting.popleft()[0], right=sorting.popleft()[0])
        for i, item in enumerate(sorting):
            if weight > item[1]:
                continue
            else:
                sorting.insert(i, (leaf, weight))
                break
        else:
            sorting.append((leaf, weight))
    return sorting[0][0]


def encode(tree, path=''):
    if not isinstance(tree, Node):
        result[tree] = path
        print(path)
    else:
        encode(tree.left, path=f'{path}0')
        encode(tree.right, path=f'{path}1')


string_to_code = "beep boop beer"
oak = tree(string_to_code)
encode(oak)

for v, i in result.items():
    print(f'{v}  =  {i}')

