"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
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
        if self.root < new_node:
            print(f'Вставляемый левый потомок должен быть меньше корня. Вставка не удалась.')
            return None
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
        if self.root > new_node:
            print(f'Вставляемый правый потомок должен быть больше корня. Вставка не удалась.')
            return None
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
r.insert_left(40)
print(r.get_left_child())
r.insert_right(5)
print(r.get_right_child())
r.insert_left(6)
print(r.get_left_child())
r.insert_right(15)
print(r.get_right_child())
'''
Для реального бинарного дерева нужна валидация по вставляемому значенеию, с рекурсивной проверкой всех узлов на 
вставку, для этого нужны ссылки на родителя, также нужна функция по удалению узла и по балансировке дерева,
а не то в один момент дерево может превратиться в список, что потеряет ценность при поиске, который станет равным O(n), 
то есть простой перебор. Также при вставке корневого значения должны быть проверены все значения в дереве на предмет
соответствия бинарному дереву.
'''