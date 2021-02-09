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
    def seek(self, code, acc):
        self.left.seek(code, acc + "0")
        self.right.seek(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def seek(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    cnt = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, cnt, Node(left, right)))

        cnt += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.seek(code, "")
    return code


def huffman_decode(encoded, code):
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)


bid = 'Dmitriy, thank you for course!'

bid_code = huffman_encode(bid)
bid_encoded = "".join(bid_code[ch] for ch in bid)
assert huffman_decode(bid_encoded, bid_code) == bid

print(bid_code)
print(bid_encoded)
print(huffman_decode(bid_encoded, bid_code))
