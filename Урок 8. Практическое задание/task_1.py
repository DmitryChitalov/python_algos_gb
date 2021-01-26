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


"""Использовал материал с сайта stepik.org. Реализация очень сложная для меня, пытался писать по памяти. Здесь исполь-
зуем модуль heapq для реализации очереди кучи (для представления очереди с приоритетами)"""


import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):  # класс для узлов дерева
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева
    def walk(self, code, acc):
        code[self.char] = acc

def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

    [(_freq, _count, root)] = h
    code = {}
    root.walk(code, "")
    return code


def main():
    s = input("Please input the string to be binary coded: ")
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(f"In the string {len(code)} unique symbols, the following code corresponds to symbol: ")
    for ch in sorted(code):
        print(f"'{ch}' - {code[ch]}")
    print(f"Coded string with length {len(encoded)} tokens: {encoded}.")


main()

