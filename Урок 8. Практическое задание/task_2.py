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

    def insert_left(self, new_node):
        if new_node >= self.root:
            print("Alert! Left child shouldn't be equal or bigger than parent")
        else:
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
                print(f'New left branch is created')
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.insert_left = self.left_child
                self.left_child = tree_obj
                print(f'New left child is created')

    def insert_right(self, new_node):
        if new_node <= self.root:
            print("Alert! Right child shouldn't be equal or lower than parent")
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
                print(f'New right branch is created')
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.insert_right = self.right_child
                self.right_child = tree_obj
                print(f'New right child is created')

    def get_right_child(self):
        if self.right_child is None:
            return 'No right child yet'
        else:
            return self.right_child

    def get_left_child(self):
        if self.left_child is None:
            return 'No left child yet'
        else:
            return self.left_child

    def set_root_val(self, obj):
        self.root = obj
        return f'Changing root value to {self.root}'

    def get_root_val(self):
        # return self.root
        return f'Root value is {self.root}'


r = BinaryTree(8)
r.insert_left(64)
r.insert_left(6)
r.insert_left(3)
print(r.get_right_child())
r.insert_right(12)
print(r.get_right_child())
r.insert_right(20)
print(r.get_left_child())
r.insert_right(2)
print(r.get_root_val())
print(r.set_root_val(17))
r.insert_right(22)
print(r.get_root_val())
print(r.get_right_child())
print(r.get_right_child().get_root_val())
print(r.get_right_child().set_root_val(16))
print(r.get_right_child().get_root_val())
print(r.get_left_child().get_root_val())
