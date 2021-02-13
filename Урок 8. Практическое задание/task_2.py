"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

class BinaryTree:
    __slots__ = ["left_child", "right_child", "value"]

    def __init__(self, i_value):
        # значение узла
        self.value = i_value
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def __str__(self):
        return f'value={self.value}'

    def insert(self, i_value):
        if i_value == self.value:
            return
        if i_value < self.value:
            if not self.left_child:
                l_obj = BinaryTree(i_value)
                self.left_child = l_obj
            else:
                self.left_child.insert(i_value)
        else:
            if not self.right_child:
                l_obj = BinaryTree(i_value)
                self.right_child = l_obj
            else:
                self.right_child.insert(i_value)

    def is_exists(self, i_value):
        if i_value == self.value:
            return True
        if i_value < self.value:
            if not self.left_child:
                return False
            else:
                return self.left_child.is_exists(i_value)
        else:
            if not self.right_child:
                return False
            else:
                return self.right_child.is_exists(i_value)


    def print_tree(self, i_pref=''):
        print(f'{i_pref}value', self.value)

        if self.left_child:
            self.left_child.print_tree(f'left-{i_pref}')

        if self.right_child:
            self.right_child.print_tree(f'right-{i_pref}')


g_tree = BinaryTree(7)
g_tree.insert(3)
g_tree.insert(8)
g_tree.insert(5)
g_tree.insert(10)
g_tree.insert(2)
g_tree.print_tree()
print('exists(5)', g_tree.is_exists(5))
print('exists(9)', g_tree.is_exists(9))
