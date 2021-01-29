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
        #количество уровней
        BinaryTree.count = 1

    def insert_val(self, value):
        # Добавил функцию вставки значения на нужное место:
        if value < self.root:
            self.insert_left(value)
        else:
            self.insert_right(value)

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if new_node > self.root:
            print("Вставка в левую ветвь значения, которое больше корня бинарного дерева невозможно")
            return
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
            BinaryTree.count += 1
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            self.left_child.insert_val(new_node)
            #tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            #tree_obj.left_child = self.left_child
            #self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if new_node < self.root:
            print("Вставка в правую ветвь значения, которое меньше корня бинарного дерева невозможно")
            return
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
            BinaryTree.count += 1
        # если у узла есть правый потомок
        else:
            self.right_child.insert_val(new_node)
            # тогда вставляем новый узел
            #tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            #tree_obj.right_child = self.right_child
            #self.right_child = tree_obj


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

r.insert_val(6)
print(r.get_left_child().get_root_val())
r.insert_val(7)
print(r.get_left_child().get_right_child().get_root_val())

r.insert_val(10)
print(r.get_right_child().get_root_val())
r.insert_val(11)
print(r.get_right_child().get_right_child().get_root_val())

print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_left(9)
print(r.get_left_child().get_root_val())

r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.insert_right(3)
print(r.get_right_child().get_root_val())

r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())


"""
Используем функцию insert_val, вставляем в правильное место в бинарном древе значения:
6
7
10
11

Защита от записи некорректных значений:
8
<__main__.BinaryTree object at 0x000002D74DBA0D00>
<__main__.BinaryTree object at 0x000002D74DBA0D00>
6
Вставка в левую ветвь значения, которое больше корня бинарного дерева невозможно - пробовали влево добавить 9, не получилось
6
<__main__.BinaryTree object at 0x000002D74E1BB700>
10
Вставка в правую ветвь значения, которое меньше корня бинарного дерева невозможно - пробовали вправо добавить 3 - не получилось
10
16
"""