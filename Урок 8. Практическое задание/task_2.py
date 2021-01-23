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
        # добавляем условие
        if new_node < self.root:
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
        # если новый элемент больше корня, то он пойдет вправо
        elif new_node > self.root:
            self.insert_right(new_node)
        # если равен, тогда ничего не делаем
        else:
            return

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node > self.root:
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
        elif new_node < self.root:
            self.insert_left(new_node)
        else:
            return

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

"""
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
"""

"""
Данный код имеет недостаток.
Создадим новый объект класса n с корнем 8
левым элемнтом 16 и правым элементом 4.
"""

n = BinaryTree(8)
n.insert_left(16)
n.insert_right(4)
print(f'Корень {n.get_root_val()}')
print(f'Левый листок {n.get_left_child().get_root_val()}')
print(f'Правый листок {n.get_right_child().get_root_val()}')

"""
Выводит:

Корень 8
Левый листок 16  ---- так было до редактирования кода
Правый листок 4  ---- так было до редактирования кода

Но так быть не должно, слева должны быть значеня меньше корня, а справа больше корня.
Попробуем исправить это.
"""

b = BinaryTree(8)
b.insert_left(16)
b.insert_right(4)
print(f'Корень после дорабобтки {b.get_root_val()}')
print(f'Левый листок после доработки {b.get_left_child().get_root_val()}')
print(f'Правый листок после доработки {b.get_right_child().get_root_val()}')

"""
Выводит:

Корень после дорабобтки 8
Левый листок после доработки 4
Правый листок после доработки 16

В методы insert_left и insert_right 
мы добавили условия длдя проверки значения new_node,
теперь, если значение new_node меньше корня, то он всегда пойдет влево,
если больше, тогда всегда вправо.
"""
