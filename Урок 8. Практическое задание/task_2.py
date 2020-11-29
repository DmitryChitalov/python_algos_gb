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
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node < self.root:
            if self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        else:
            print('Вы пытаетесь добавить в левую ветку элемент больше корневого')

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node >= self.root:
            if self.right_child == None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        else:
            print('Вы пытаетесь добавить в правую ветку элемент меньше корневого')

    # метод доступа к правому потомку
    def get_right_child(self):
        if self.right_child is None:
            return 'Правая ветка пуста'
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child is None:
            return 'Левая ветка пуста'
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def get_left(self):
        try:
            return r.get_left_child().get_root_val()
        except AttributeError:
            return 'Левая ветка пуста'

    def get_right(self):
        try:
            return r.get_right_child().get_root_val()
        except AttributeError:
            return 'Правая ветка пуста'


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(14)
print(r.get_left_child())
print(r.get_left())
r.insert_left(4)
r.insert_right(12)
r.insert_right(2)
print(r.get_right_child())
print(r.get_right())
print(r.get_left())

"""Добавил в insert_left и insert_right условия проверки для подаваемых значений, теперь программа 
выдает предупреждение, если оно больше или меньше для каждой ветки.
Также дописал функции, в которых происходит обработка запроса значений в левой и правой ветках. get_left и get_right
В них есть блок try except, на случай если ветка пуста.
Раньше программа падала, т.к. если значения в ветке не было, то не было и метода get_root_val у соответсвующей ветки.
Сейчас при запросе значения в пустой ветке программа выдает сообщение, что ветка пуста.

8
Левая ветка пуста
Вы пытаетесь добавить в левую ветку элемент больше корневого
Левая ветка пуста
Левая ветка пуста
Вы пытаетесь добавить в правую ветку элемент меньше корневого
<__main__.BinaryTree object at 0x0000026414FF6F10>
12
4
"""