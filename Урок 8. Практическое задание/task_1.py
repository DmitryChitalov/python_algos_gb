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

from heapq import heapify
from heapq import heappop
from heapq import heappush
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def go(self, code, acc):
        self.left.go(code, acc + "0")
        self.right.go(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def go(self, code, acc):
        code[self.char] = acc or "0"


def huffman(s):  #
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapify(h)
    count = len(h)
    while len(h) > 1:
        f1, _count1, left = heappop(h)
        f2, _count2, right = heappop(h)

        heappush(h, (f1 + f2, count, Node(left, right)))

        count += 1
    code = {}
    if h:  #
        [(_freq, _count, root)] = h
        root.go(code, "")
    return code


def main():
    s = "first second third!"
    code = huffman(s)
    encoded = "".join(code[ch] for ch in s)

    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)
