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

    def insert(self, new_node):
        if new_node > self.get_root_val():
            self.insert_right(new_node)
            print('insert right')
        else:
            self.insert_left(new_node)
            print('insert left')

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
# и спускаем имеющегося потомка на один уровень ниже, если потомок меньше нового узла, либо передаем потомку новый узел
            if tree_obj.root < self.root:
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            else:
                self.left_child.insert(new_node)

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            tree_obj = BinaryTree(new_node)
# и спускаем имеющегося потомка на один уровень ниже, если потомок больше нового узла, либо передаем потомку новый узел
            if tree_obj.root > self.root:
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
            else:
                self.right_child.insert(new_node)

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

    def __str__(self):
        return f'root:{self.root} right:{self.right_child.__str__()} left:{self.left_child.__str__()}'


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert(40)
print(r.get_left_child())
print(r.get_left_child())
r.insert(12)
print(r.get_right_child().get_right_child().get_root_val())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
r.insert(5)
r.insert(33)
r.insert(1)
r.insert(51)

print(r)
"""
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)
1. для добавления потомка добавить метод insert, и в нем выбирать куда добавлять - влево или вправо:
    def insert(self, new_node):
        if new_node > self.get_root_val():
            self.insert_right(new_node)
            print('insert right')
        else:
            self.insert_left(new_node)
            print('insert left')
2. при добавлении узла проверяем, добавить его вместо текущего потомка или передать этот узел потомку,
модифицируем insert_left() и insert_right() по аналогии. :
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            if tree_obj.root > self.root:
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            else:
                self.left_child.insert(new_node)
3. set_root_val() тоже требуется доработка: при изменении необходимо проверять правильность положения ноды в 
соответствии с новым значением 



Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде. - выполнено, результат:
8
None
insert right
None
None
insert right
40
12
16
insert left
insert right
insert left
insert right
  root:8 right:  root:51 right:  root:33 right:  root:16 right:  root:40 right:None left:None left:None left:None left:None left:  root:1 right:None left:  root:5 right:None left:None
"""
