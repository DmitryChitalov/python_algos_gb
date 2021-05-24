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

    def __str__(self):
        return str(self.root)

    def insert_left(self, new_node):
        if new_node > self.root:
            print(f'Элемент слева ({new_node}) должен быть меньше корня ({self.root})!')
            return
        if self.left_child:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
        else:
            self.left_child = BinaryTree(new_node)

    def insert_right(self, new_node):
        if new_node < self.root:
            print(f'Элемент справа ({new_node}) должен быть больше корня ({self.root})!')
            return
        if self.right_child:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
        else:
            self.right_child = BinaryTree(new_node)

    def get_depth(self):
        depth_left = 0 if self.left_child is None else self.left_child.get_depth() + 1
        depth_right = 0 if self.right_child is None else self.right_child.get_depth() + 1
        return max(depth_left, depth_right)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(6)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
r.insert_left(2)
r.insert_left(4)
print(r.get_left_child())
# print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
# print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(14)
print(r.get_right_child().get_root_val())
print(f'Глубина дерева: {r.get_depth()}')
