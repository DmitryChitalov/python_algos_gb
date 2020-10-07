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
        if not isinstance(new_node, int):
            raise ValueError("The value must be a number")
        if self.root < new_node:
            raise ValueError("The left child cannot be greater than the root value")
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            if new_node > self.left_child.root:
                tree_obj.right_child = self.left_child
            else:
                tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if not isinstance(new_node, int):
            raise ValueError("The value must be a number")
        if self.root > new_node:
            raise ValueError("The right child cannot be less than the root value")
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            if new_node > self.right_child.root:
                tree_obj.right_child = self.right_child
            else:
                tree_obj.left_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        if not isinstance(obj, int):
            raise ValueError("The value must be a number")
        if self.right_child and obj > self.right_child.root:
            raise ValueError("The right child cannot be less than the root value")
        if self.left_child and obj < self.left_child.root:
            raise ValueError("The left child cannot be greater than the root value")
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def get_left_child_val(self):
        if self.left_child:
            return self.left_child.root
        else:
            return None

    def get_right_child_val(self):
        if self.right_child:
            return self.right_child.root
        else:
            return None


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child_val())
"""Сделана валидация значений узлов в соответствии с требованиями для бинарного дерева, добавлены методы получения 
значений потомков"""
