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
        if new_node > self.root:
            print(f'Enter number < {self.root} for the Left side')
        else:
            if self.left_child is None:
                # если у узла нет левого потомка
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
                # если у узла есть левый потомок
            elif new_node < self.left_child.get_root_val():
                print(f'Enter number between {self.left_child.get_root_val()} - {self.root} for the Left side')
            elif new_node == self.left_child.get_root_val():
                print(f'Number {new_node} already exists')
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            print(f'Enter number > {self.root} for the Right side')
        else:
            if self.right_child is None:
                # если у узла нет правого потомка
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            elif new_node < self.right_child.get_root_val():
                print(f'Enter number between {self.root} - {self.right_child.get_root_val()} for the Right side')
            elif new_node == self.right_child.get_root_val():
                print(f'Number {new_node} already exists')
            else:
                # если у узла есть правый потомок
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
        if self.left_child is None and self.right_child is None:
            self.root = obj
        else:
            print(f"You can't change root, since Children already set")

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
r.set_root_val(20)
print(r.get_root_val())
r.insert_left(5)
r.insert_left(3)
r.insert_right(25)
r.insert_right(24)
r.insert_right(2)
r.insert_right(22)
