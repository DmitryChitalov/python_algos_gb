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
import heapq  # Модуль очередей с приоритетами
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")  # Префикс кода который мы накопили спускаясь от корня до данного узла или листа
        # Чтобы обойти внутренний вызов нам нужно спустится вначале в левого потомка, добавив к префиксу 0
        self.right.walk(code, acc + "1")  # А сюда добавим к префиксу 1


class Leaf(namedtuple("Leaf", ["char"])):  # Никаких потомков у листа нет
    def walk(self, code, acc):  # Запишем в словарь code построенный код данного символа
        code[self.char] = acc


def huffman(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))  # Первый компонент freq это частота, второй len это счетчик
        # который должен быть уникальным для всех листьев, третий компонент это лист.
        # Для всех листов в списке h второй компонент различен
    heapq.heapify(h)  # Очередь с приоритетами
    count = len(h)  # Инициализируем его размером нашей очереди с приоритетами
    while len(h) > 1:  # До тех пор пока в очереди есть 2 элемента
        freq1, _count1, left = heapq.heappop(h)  # Достаем элемент с минимальной частотой
        freq2, _count2, right = heapq.heappop(h)  # и след. за ним элемент с мин. частотой
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # А затем добавляем в очередь новый
        # элемент у которого частота является суммой частот 2 элементов которые мы уже вытащили
        count += 1
    [(_freq, _count, root)] = h  # Корень построенного дерева
    code = {}
    root.walk(code, "")  # Дерево обходим начиная с корня, и заполнить словарь code
    return code


user_input = "la la land"
code = huffman(user_input)
encoded = ' '.join(code[ch] for ch in user_input)
for ch in sorted(code):
    print('{}: {}'.format(ch, code[ch]))
print(encoded)

"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node > self.root:
            return print("Нарушение требований бинарного дерева!")
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            return print("Нарушение требований бинарного дерева!")
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

# Проверка валидации
r.insert_left(33)
r.insert_right(1)
