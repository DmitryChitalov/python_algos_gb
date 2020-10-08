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


class Node(namedtuple("Node", ["left", "right"])): # Класс для узлав
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])): # Класс для листьев
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_tree(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapify(h) # создаем очередь с приоритетом
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heappop(h) # достаем минимальный элемент
        freq2, _count2, right = heappop(h) # достаем второй минимальный элемент
        # переменная count нужна для сортировки, поэтому она уникальная
        heappush(h, (freq1 + freq2, count, Node(left, right)))
        
        count += 1
    if h:
        [(_freq, _count, root)] = h # вытаскиваем дерево
        return root
    else:
        return []
    
    
def huffman_code(tree_root):
    code = {}
    if tree_root:
        tree_root.walk(code, "")
    return code


if __name__ == "__main__":
    string = input()
    code = huffman_code(huffman_tree(string))
    encoded = "".join(code[symbol] for symbol in string)
    
    for sym in sorted(code):
        print(f'{sym}: {code[sym]}')
    print(encoded)
