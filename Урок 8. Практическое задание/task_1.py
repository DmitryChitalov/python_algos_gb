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

from collections import Counter, deque
from numpy import array


class BinaryTree:
    __slots__ = array(['root', 'value', 'parent', 'left_child', 'right_child'])

    def __init__(self, root_obj, val=None, parent=None):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

        self.value = val

        self.parent = parent

    # добавить левого потомка
    def insert_left(self, new_node, new_val=None):
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node, new_val, self)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, new_val, self)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node, new_val=None):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node, new_val, self)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, new_val, self)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def set_node_left(self, other):
        self.left_child = other

    def set_node_right(self, other):
        self.right_child = other

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

    def get_parent(self):
        return self.parent

    def set_parent(self, new_parent):
        self.parent = new_parent

    def got_both_children(self):
        if self.left_child and self.right_child:
            return True
        return False


class HaffmanTree:
    __slots__ = array(['obj_to_code', 'tree', 'last_left_node', 'last_right_node', 'encoded_symbols'])

    def __init__(self, obj_to_code):
        self.obj_to_code = obj_to_code
        self.tree = BinaryTree(len(obj_to_code))

        self.last_left_node = None
        self.last_right_node = None

        self.encoded_symbols = {}

    def merge_nodes(self, node_left, node_right):
        parent = node_left.get_parent()
        parent.insert_left(node_left.get_root_val() + node_right.get_root_val())
        parent.set_node_right(None)
        node_left.set_parent(parent.get_left_child())
        parent = node_left.get_parent()
        parent.set_node_right(node_right)
        node_right.set_parent(parent.get_left_child())
        self.last_right_node = None

    def append_to_haffman_tree(self, tree, new_node, direction=0):
        if new_node[1] < tree.get_root_val():
            if tree.get_left_child() is None:
                tree.insert_left(new_node[1], new_node[0])
            else:
                if tree.got_both_children():
                    cur_tree_parent = tree.get_parent()
                    if cur_tree_parent is None:
                        cur_tree_parent = tree
                    if cur_tree_parent.get_right_child() is None:
                        cur_tree_parent.insert_right(new_node[1], new_node[0])
                    else:
                        self.append_to_haffman_tree(cur_tree_parent.get_right_child(), new_node, 1)
                else:
                    self.append_to_haffman_tree(tree.get_left_child(), new_node, 0)
        else:
            if direction == 1:
                tree.parent.insert_right(tree.get_root_val() + new_node[1])
                tree.parent.get_right_child().insert_left(new_node[1], new_node[0])
                tree.parent = tree.parent.get_right_child()
                self.last_right_node = tree.parent
            else:
                tree.parent.insert_left(tree.get_root_val() + new_node[1])
                tree.parent.get_left_child().insert_right(new_node[1], new_node[0])
                tree.parent = tree.parent.get_left_child()
                self.last_left_node = tree.parent
            if new_node[1] == tree.get_root_val() and self.last_right_node and self.last_left_node and \
                    self.last_right_node.get_root_val() == self.last_left_node.get_root_val():
                self.merge_nodes(tree.parent.parent.get_left_child(), tree.parent.parent.get_right_child())

    def find_elements_codes(self, node=None, prev_directions=''):
        if node is None:
            node = self.tree
        node_left_child = node.get_left_child()
        node_right_child = node.get_right_child()
        if node_left_child is None and node_right_child is None:
            if node.value is not None:
                self.encoded_symbols.update({node.value: prev_directions})
            else:
                pass
            return
        if node_left_child is not None:
            self.find_elements_codes(node_left_child, prev_directions + '0')
        if node_right_child is not None:
            self.find_elements_codes(node_right_child, prev_directions + '1')

    def encode(self):
        count = Counter(self.obj_to_code)
        sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
        for cortege in sorted_elements:
            self.append_to_haffman_tree(self.tree, cortege)
        self.find_elements_codes()

    def encoded(self):
        if self.encoded_symbols is None:
            self.encode()


s = "beep boop beer!"
class_obj = HaffmanTree(s)

class_obj.encode()

for symb in s:
    print(class_obj.encoded_symbols[symb], end=' ')

# 11 10 10 001 011 11 010 010 001 011 11 10 10 0000 0001
# Вывод: кодировка отличается от той, что была дана на уроке, но если все работает верно. Реализация данной функции
# через классы не лучший вариант, тк затрачивается больше ресурсов компьютера. (как минимум создается больше объектов
# класса)
