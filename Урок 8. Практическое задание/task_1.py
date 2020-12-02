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

import collections
import operator


class Leaf:

    def __init__(self, char: str, *value: int):
        if isinstance(char, tuple):
            self.char, self.value = char
        else:
            self.char = char
            self.value = value

    def __repr__(self):
        return f'Leaf: char "{self.char}" value {self.value}'


class Node:

    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node: value {self.value} \nleft->{self.left} \nright->{self.right}'


class Haffman:

    def __init__(self):
        self._code_table = {}

    def _get_table(self, tree, code=''):

        if isinstance(tree, Node):
            self._get_table(tree.left, code=f'{code}0')
            self._get_table(tree.right, code=f'{code}1')
        elif isinstance(tree, Leaf):
            self._code_table[tree.char] = code

    def encode(self, string, detail=False):
        self._code_table = {}
        count = collections.Counter(string)
        array = collections.deque(map(Leaf, count.most_common()))
        if detail:
            print(array)

        while len(array) > 1:
            array = collections.deque(sorted(array, key=operator.attrgetter('value')))
            leaf_small = array.popleft()
            leaf_bigger = array.popleft()
            array.append(Node(leaf_small.value + leaf_bigger.value, leaf_small, leaf_bigger))

        tree = array.pop()
        if detail:
            print(tree)

        self._get_table(tree)
        if detail:
            print(self._code_table)


        return ' '.join([self._code_table[char] for char in string])


haff = Haffman()
print(haff.encode('мама мыла раму', detail=True))


