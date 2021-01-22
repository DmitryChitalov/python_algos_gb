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

import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for el, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(el)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _1, left = heapq.heappop(h)
        freq2, _2, right = heapq.heappop(h)

        heapq.heappush(h, ((freq1 + freq2), count, Node(left,right)))
        count += 1
    code = {}
    if h:
        [(_freq, _1, root)] = h
        root.walk(code, "")
    return code

def main(s):
    code = huffman_encode(s)
    return "".join(code[el] for el in s)


if __name__ == '__main__':
    s = "beep boop beer!"
    print(main(s))
