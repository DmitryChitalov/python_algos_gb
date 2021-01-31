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
from collections import Counter
from collections import namedtuple


class Nodes(namedtuple("Node", ['left', 'right'])):  # класс для ветвей дерева
    def path(self, code, acc):
        self.left.path(code, acc + "0")
        self.right.path(code, acc + "1")


class Leaf(namedtuple("Leaf", ['sym'])):  # класс для листьев, здесь значения
    def path(self, code, acc):
        code[self.sym] = acc or 0


def hufencode(words):  # функция для кодирования(сжатия)
    e_sym = []  # очередь с приоритетами
    for sym, times in Counter(words).items():
        e_sym.append(
            (times, len(e_sym), Leaf(sym)))  # times-частоста символа,его счетчик-len(e_sym),сам символ-Leaf(sym)
    heapq.heapify(e_sym)
    count = len(e_sym)  # выставляем значение счетчика равным длине очереди
    while len(e_sym) > 1:  # действует пока в очереди хотя бы 2 элемента
        times1, _count1, left = heapq.heappop(e_sym)  # символ с мин частотой в левый узел
        times2, _count2, right = heapq.heappop(e_sym)  # след символ с мин частотой в правый узел
        heapq.heappush(e_sym, (times1 + times2, count, Nodes(left, right)))  # новый узел с потомками
        count += 1  # инкремент счетчика
    code = {}
    if e_sym:
        [(_times, _count, root)] = e_sym
        root.path(code, "")
    return code


def hufdecode(encoded, code):  # функция расшифровки исходногй строки
    de_sym = []  # пустой массив, в него добавляем расшифрованные символы
    enc_sym = ""
    for sym in encoded:
        enc_sym += sym  # добавляем символ к строке закодированного  символа
        for dec_sym in code:  # ищем совпадения в словаре кодов
            if code.get(dec_sym) == enc_sym:
                de_sym.append(dec_sym)  # добавляем значение раскодированного символа
                enc_sym = ""  # обнуляем значение символа
                break
    return "".join(de_sym)


words = input("Введите текст: ")
code = hufencode(words)
encoded = "".join(code[sym] for sym in words)
print(encoded)
print(hufdecode(encoded, code))
