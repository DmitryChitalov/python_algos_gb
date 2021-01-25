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


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    print(h)
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _c1, left = heapq.heappop(h)
        freq2, _c2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


s = "beep boop beer!"
code = huffman_encode(s)
encoded = " ".join(code[ch] for ch in s)
print(len(code), len(encoded))
for ch in sorted(code):
    print(f"{ch}: {code[ch]}")

print(encoded)