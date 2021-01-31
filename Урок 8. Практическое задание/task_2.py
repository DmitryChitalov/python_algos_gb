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

    # добавить потомка
    def insert(self, new_node):
        if new_node > self.root:
            # print(f"{new_node} добавлен в правую часть дерева")
            if self.right_child == None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj

        else:
            # print(f"{new_node} добавлен в левую часть дерева")
            if self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj


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
print(r.get_root_val())
print(r.get_left_child())
r.insert(4)
r.insert(5)
r.insert(2)
r.insert(1)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert(12)
r.insert(16)
r.insert(13)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
