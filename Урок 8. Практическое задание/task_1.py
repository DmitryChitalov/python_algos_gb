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
from collections import Counter, deque


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def get_tree(tree):
    if isinstance(tree, str):
        tree = Counter(tree)
        tree = deque(sorted(tree.items(), key=lambda x: x[1]))
        return get_tree(tree)
    if len(tree) < 2:
        return get_code(tree.pop()[0])
    left = tree.popleft()
    right = tree.popleft()
    tree.appendleft((Node(left[0], right[0]), left[1] + right[1]))
    tree = deque(sorted(tree, key=lambda x: x[1]))
    return get_tree(tree)


def get_code(node, code=''):
    if isinstance(node, str):
        return {node: code}
    children = node.children()
    result = dict()
    result.update(get_code(children[0],  code + '0'))
    result.update(get_code(children[1],  code + '1'))
    return result


STR = 'beep boop beer!'
print(f'Исходная строка - {STR}')
print('Результат - '+" ".join([get_tree(STR)[elm] for elm in STR]))

