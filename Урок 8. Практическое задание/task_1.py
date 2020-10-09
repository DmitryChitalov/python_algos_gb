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
    def move(self, code, set_s):
        self.left.move(code, set_s + "0")
        self.right.move(code, set_s + "1")
class Leaf(namedtuple("Leaf", ["sign"])):
    def move(self, code, set_s):
        code[self.sign] = set_s or "0"  # ноль для того чтобы не вылететь, если будет  введено только "a"

def haffm_enc(s):
    h = []
    for el, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(el))) # len(h) - это счетчик
        print(f'Очередь: {h}')

    heapq.heapify(h)
    count = len(h)
    while len(h) > 1: #  пока в очереди есть хотя бы два элемента
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:                               #  тут на случай пустой строки
        [(_freq, _count, root)] = h
        root.move(code, "")
    return code

def main():
    s = input('Строка: ')
    code = haffm_enc(s)
    print(f'code: {code}')
    res = ' '.join(code[i] for i in s) # закодированная строка

    print(f'Количество ключей: {len(code)}, Длина закодированной строки: {len(res)}')
    #for el in code:
    #   print(f"{el} : {code[el]}")
    print(res)

main()



