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


    def insert_left(self, new_node):

        if self.left_child == None:
            # проверка валидности
            if new_node < self.root:
                self.left_child = BinaryTree(new_node)
            else:
                new_node = int(input(f'Введите число меньше {self.root} '))
                self.left_child = BinaryTree(new_node)
        else:
            # проверка валидности
            if new_node < self.left_child.root:
                tree_obj = BinaryTree(new_node)
            else:
                new_node = int(input(f'Введите число меньше {self.left_child.root} '))
                tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj


    def insert_right(self, new_node):

        if self.right_child == None:
            # проверка валидности
            if new_node > self.root:
                self.right_child = BinaryTree(new_node)
            else:
                new_node = int(input(f'Введите число больше {self.root} '))
                self.right_child = BinaryTree(new_node)
        else:
            # проверка валидности
            if new_node > self.right_child.root:
                tree_obj = BinaryTree(new_node)
            else:
                new_node = int(input(f'Введите число больше {self.right_child.root} '))
                tree_obj = BinaryTree(new_node)
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
'''В алгоритм добавленна проверка валидности вставляемых значений. Для левого потомка только 
меньшие значения. Для правого - только большие значения. Проверенно на тестах ниже'''

r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(8)
print(r.get_left_child())
r.insert_left(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(7)
print(r.get_right_child())
r.insert_right(7)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
