"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
from collections import namedtuple
from collections import Counter
import heapq

my_str = "Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения и " \
         "оптимизации. "


# посчитаем частоту каждого символа
def get_frequency_each_character(str):
    return Counter(str)

# хранение информации о дереве
class Node(namedtuple("Node", ["left", "right"])):
    # ветви
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

# хранение информации о листьях
class Leaf(namedtuple("Leaf", ["char"])):
    # листья не имеют потомков
    def walk(self, code, acc):
        code[self.char] = acc or "0"


# кодирование строки
def huffman_encode(s):
    huff_queue = []
    code = {}
    # получим частоту каждого символа
    for ch, freq in Counter(s).items():
        huff_queue.append((freq, len(huff_queue), Leaf(ch)))

    heapq.heapify(huff_queue)
    count = len(huff_queue)

    while len(huff_queue) > 1:
        # левый элемент с минимальной частотой
        freq1, _count1, left = heapq.heappop(huff_queue)
        # правый элемент с минимальной частотой
        freq2, _count2, right = heapq.heappop(huff_queue)
        heapq.heappush(huff_queue, (freq1 + freq2, count, Node(left, right)))
        count += 1

    if huff_queue:
        [(_freq, _count, root)] = huff_queue
        root.walk(code, "")

    return code

# дэкодирование строки
def huffman_decode(encoded, code):
    decoded_str = []
    encode_ch = ""
    for ch in encoded:
        encode_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == encode_ch:
                decoded_str.append(dec_ch)
                encode_ch = ""
                break

    return "".join(decoded_str)


if __name__ == '__main__':
    print("- " * 50)
    print("from Counter: {}".format(get_frequency_each_character(my_str)))
    code = huffman_encode(my_str)
    encoded = "".join(code[ch] for ch in my_str)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))

    print(encoded)
    print("- " * 50)
    print("{}".format(huffman_decode(encoded, code)))