"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""
import sys


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        self.value = root_obj

    def __str__(self):
        return f'value = {self.value}'

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            if new_node >= self.get_root_val():
                print(
                    f'Ошибка добавления узла в левой части. Потомок {new_node}'
                    f' должен быть меньше родителя {self.get_root_val()}')
                sys.exit()
            self.left_child = BinaryTree(new_node)


        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
        print(self.left_child)

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево

            if new_node <= self.get_root_val():
                print(
                    f'Ошибка добавления узла в правой части. Потомок {new_node} '
                    f' должен быть больше родителя {self.get_root_val()}')
                sys.exit()
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
        print(self.right_child)

    # метод доступа к правому потомку
    def get_right_child(self):
        print(f'right_child: {self.right_child}')
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        print(f'left_child: {self.left_child}')
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        print(f'установка root: {self.root}')
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        print(f'root: {self.root}')
        return self.root


r = BinaryTree(8)
r.insert_left(4)
r.insert_right(12)

r.insert_left(2)

r.insert_right(6)
r.insert_left(1)
r.insert_right(3)

r.get_left_child().set_root_val(6)

r.insert_left(5)
r.insert_right(7)

r.get_left_child().set_root_val(12)
r.insert_left(10)
r.insert_right(14)

"""
root: 8
value = 4
root: 8
value = 12
value = 2
value = 6
value = 1
value = 3
left_child: value = 1
установка root: 1
value = 5
value = 7
left_child: value = 5
установка root: 5
value = 10
value = 14

------------
Пытаемся вставить в левой  части значение 25

r = BinaryTree(8)
r.insert_left(25)
r.insert_right(12)

root: 8
root: 8
Ошибка добавления узла в левой части. Потомок 25 должен быть меньше родителя 8


___________
Пытаемся вставить в правой части значение 7
r = BinaryTree(8)
r.insert_left(4)
r.insert_right(7)

root: 8
value = 4
root: 8
root: 8
Ошибка добавления узла в правой части. Потомок 7  должен быть больше родителя 8

"""
