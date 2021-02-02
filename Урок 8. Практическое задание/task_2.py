"""
Задание 2.

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

    def print_tree(self, level=1):
        if self.root is not None:
            if self.right_child is not None:
                self.right_child.print_tree(level + 1)
            print(' ' * 4 * level + '->', self.root)
            if self.left_child is not None:
                self.left_child.print_tree(level + 1)

    def insert(self, new_node):
        if self.root == new_node:
            raise ValueError
        elif self.root < new_node:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                self.right_child.insert(new_node)
        else:  # self.root >= new_node
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                self.left_child.insert(new_node)

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        # необходимо проверить соответствие нового значения условиям по дочерним узлам
        left_child = self.get_left_child()
        if left_child and left_child.get_root_val() >= obj:
            raise ValueError(f'set_root_val: invalid left child for {obj}')
        right_child = self.get_right_child()
        if right_child and right_child.get_root_val() < obj:
            raise ValueError(f'set_root_val: invalid right child for {obj}')
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
lst = [4, 12, 3, 5, 11, 25]
try:
    for el in lst:
        r.insert(el)
    r.get_right_child().set_root_val(16)
except ValueError as err:
    print(f'Неверное значение для узла {str(err)}')

print(r.print_tree(1))
