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

from collections import Counter
from heapq import heapify, heappop, heappush

from string import hexdigits


class Node:
    # Элемент дерева символов для алгоритма Хаффмана. Содержит символ текста,
    # частоту его повторения и массив непосредственных потомков в дереве.
    # Объекты можно сравнивать. Сравнение производится по частоте повторения,
    # либо по номерам символов в Unicode, если частоты равны:
    # >>> Node('z', freq=90) > Node('b', freq=20)
    # >>> True
    # >>> Node('z', freq=30) < Node('b', freq=20)
    # >>> False
    # >>> Node('a', freq=20) < Node('n', freq=20)
    # >>> True

    def __init__(self, letter=None, freq=0, children=None):
        self.letter = letter
        self.freq = freq
        self.children = children or []

    def tuple(self):
        return self.freq, ord(self.letter) if self.letter else -1

    def __lt__(self, other):
        return self.tuple() < other.tuple()

    def __eq__(self, other):
        return self.tuple() == other.tuple()


def encoding_table(node, code=''):
    # Превращает построенное алгоритмом Хаффмана дерево
    # в словарь соответствия символ-код.
    # Для кодирования, в зависимости от арности дерева,
    # используются символы [0-9abcdef].
    # :param node: корень дерева
    # :param code: префикс всех кодов (при вызове оставить пустым)
    # :return: словарь соответствия символ-код.
    # >>> encoding_table(Node(children=[Node('a'), Node('b'), Node('c')]))
    # >>> {'a': '0', 'b': '1', 'c': '2'}

    if node.letter is None:
        mapping = {}
        for child, digit in zip(node.children, hexdigits):
            mapping.update(encoding_table(child, code + digit))
        return mapping
    else:
        return {node.letter: code}


def huffman_encode(text, arity=2):
    # Кодирует строку текста алгоритмом Хаффмана с заданным
    # количеством символов выходного алфавита
    # :param text: текст для кодирования
    # :param arity: количество символов выходного алфавита (от 2 до 16)
    # :return: tuple: (<дерево декодирования>, <закодированная строка>)
    # >>> huffman_encode('helloworld', 2)
    # >>> (<utils.Node object...>, '000101111110110001001111010')
    # >>> huffman_encode('abcdefghijklmnop', 16)
    # >>> (<utils.Node object...>, '0123456789abcdef')

    nodes = [Node(letter, freq) for letter, freq in Counter(text).items()]
    heapify(nodes)

    # Строит n-арное дерево
    while len(nodes) > 1:
        list_children = [heappop(nodes) for _ in range(arity)]
        freq = sum([node.freq for node in list_children])

        node = Node(None, freq)
        node.children = list_children

        heappush(nodes, node)

    root = nodes[0]
    codes = encoding_table(root)

    return root, ''.join([codes[letter] for letter in text])


inp = input("Сообщение к шифровке:\n")
out = huffman_encode(inp)[1]
print(out)
