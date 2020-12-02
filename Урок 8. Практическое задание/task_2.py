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
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        else:
            return print(f'Левый потомок не может быть больше корня!')

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
            return print(f'Правый потомок не может быть меньше корня!')

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


r = BinaryTree(16)
r.insert_left(10)
r.insert_right(20)
r.get_left_child().insert_right(30)

print(r.get_root_val())
print(r.get_left_child().get_root_val())
# print(r.get_left_child().get_left_child().get_root_val())
print(r.get_left_child().get_right_val())
# r.insert_right(12)
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val(16)
# print(r.get_right_child().get_root_val())


