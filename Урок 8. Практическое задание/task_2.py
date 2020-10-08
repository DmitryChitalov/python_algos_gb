"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class LeftChild(Exception):
    pass


class RightChild(Exception):
    pass


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
        # если у узла нет левого потомка
        if self.left_child is None:
            if new_node < self.root:

            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            else:
                raise LeftChild(Exception)
        # если у узла есть левый потомок
        else:
            if new_node < self.left_child.root:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            else:
                raise LeftChild(Exception)

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            if new_node > self.root:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            else:
                raise RightChild(Exception)
        # если у узла есть правый потомок
        else:
            if new_node > self.right_child.root:

                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
            else:
                raise RightChild(Exception)
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
r.insert_left(2)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.insert_right(13)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(14)
print(r.get_right_child().get_root_val())
