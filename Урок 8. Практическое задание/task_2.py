"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""
'''
Доработал дерево потомки рапределяются относительно корневого узла влево и вправо. И далее относительно
каждого узла ветвятся и распределяются влево или вправо. Единственно не соблюдается иерархия что бы все потомки 
были по убывающей. Сейчас они только те кто меньше середины те расположены слева и те кто больше те справа.
И относительно своих узлов слева и справа в зависимости от значения.
'''

import random

my_list = [random.randint(0, 50) for _ in range(11)]

class MyBinaryTree:

    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left = None
        # правый потомок
        self.right = None

    # добавляем новый элемент дерева
    def insert(self, data):
        # если есть значение узла проверяем в право или лево отправить
        if self.root:
            if data < self.root:
                if self.left is None:
                    self.left = MyBinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.root:
                if self.right is None:
                    self.right = MyBinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.root = data

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left

    # метод доступа к корню
    def get_root_val(self):
        return self.root


tree = MyBinaryTree(25)

for i in my_list:
    tree.insert(i)

print(my_list)
print(tree.get_root_val())
print(tree.get_left_child())
print(tree.get_right_child())
