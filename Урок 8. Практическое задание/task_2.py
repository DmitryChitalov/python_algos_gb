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

    def __str__(self):
        return f'({self.left_child}, {self.root}, {self.right_child})'

    def has_children(self):
        return self.right_child is not None or self.left_child is not None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
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
        # если у узла нет правого потомка
        if self.right_child is None:
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
print(r)

# Добавлен метод __str__. Было:
# ---
# 8
# None
# <__main__.BinaryTree object at 0x7fd1e107cf70>
# 4
# <__main__.BinaryTree object at 0x7fd1e107cd30>
# 12
# 16
# <__main__.BinaryTree object at 0x7fd1e107cfd0>
# ---

# Стало:
# ---
# 8
# None
# (None, 4, None)
# 4
# (None, 12, None)
# 12
# 16
# ((None, 4, None), 8, (None, 16, None))
# ---

# Также добавлен метод has_children(), необходимый для
# рекурсивных механизмов обхода

# Предложение по API класса.
# Если get_*_child() возвращает значение
# не в виде числа, а в виде BinaryTree, метод
# insert_* тоже должен получать BinaryTree.
# Методы, которые сейчас называются insert_*
# нужно переименовать в create_*

# Модифицированный класс используется в самообучающейся
# программе по классификации животных (task_3.py)
