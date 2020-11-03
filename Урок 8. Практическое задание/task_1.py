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

from heapq import heapify, heappop, heappush
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):  # класс для ветвей дерева - внутренних узлов
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):  # Класс для листьев  у него нет потомков, но есть значение символа
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapify(h)  # создаем очередь с приоритетом
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heappop(h)  # достаем минимальный элемент - левый узел
        freq2, _count2, right = heappop(h)  # достаем второй минимальный элемент - правый узел
        # переменная count нужна для сортировки, поэтому она уникальная
        heappush(h, (freq1 + freq2, count, Node(left, right)))

        count += 1
    if h:
        [(_freq, _count, root)] = h  # вытаскиваем дерево
        return root
    else:
        return []


def huffman_code(tree_root):
    code = {}
    if tree_root:
        tree_root.walk(code, "")
    return code


def huffman_decode(encoded, code):  # функция декодирования исходной строки по кодам Хаффмана
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


if __name__ == "__main__":

    string = input('Введите строку:')
    code = huffman_code(huffman_encode(string))
    encoded = "".join(code[symbol] for symbol in string)

    for sym in sorted(code):
        print(f'{sym}: {code[sym]}')
    print(f'Закодированная строка: {encoded}')

    print(f"Раскодированная строка: {huffman_decode(encoded, code)}")
