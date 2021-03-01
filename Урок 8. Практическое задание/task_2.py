"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
"""
Хотела доработать дерево бинарное. Какое-то время полностью его переписывала (создавала доп класс node), но осознав, 
    что просто не успеваю откатила все обратно
Освежила недавно приобретенные знания по создание своих собственных исключений.
"""


class BinaryNodeException(BaseException):

    def __init__(self, node):
        self.node = node

    def __str__(self):
        print(f"incorrect insert of {self.node} in the Binary tree")


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
            print(f"Вы пытаетесь добавить {new_node} в левую ветку {self.root}")
            raise BinaryNodeException(new_node)
        else:
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

    # добавить правого потомка
    def insert_right(self, new_node):

        if self.root > new_node:
            print(f"Вы пытаетесь добавить {new_node} в правую ветку {self.root}")
            raise BinaryNodeException(new_node)
        else:
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
try:
    r.insert_left(6)
except BinaryNodeException:
    exit()

print(r.get_root_val())
print(r.get_left_child())
print(r.get_left_child().get_root_val())
try:
    r.insert_right(12)
except BinaryNodeException:
    exit()

print(r.get_left_child())
r.get_right_child().set_root_val(12)
try:
    r.insert_right(40)
except BinaryNodeException:
    exit()
print(r.get_left_child())
print(r.get_left_child().get_root_val())
try:
    r.insert_left(32)
except BinaryNodeException:
    exit()
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
print(r.get_right_child().get_root_val())
