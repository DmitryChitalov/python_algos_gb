"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root):
        self.__root = root
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.__root)

    def insert_left(self, new_node):
        try:
            if self.__root >= new_node:
                if self.left_child is None:
                    self.left_child = BinaryTree(new_node)
                else:
                    tree = BinaryTree(new_node)
                    tree.left_child = self.left_child
                    self.left_child = tree
            else:
                raise Exception(f'Ошибка при попытке вставки элемента: {self.__root} меньше, чем {new_node}')
        except Exception as e:
            print(e)

    def insert_right(self, new_node):
        try:
            if self.__root <= new_node:
                if self.right_child is None:
                    self.right_child = BinaryTree(new_node)
                else:
                    tree = BinaryTree(new_node)
                    tree.right_child = self.right_child
                    self.right_child = tree
            else:
                raise Exception(f'Ошибка при попытке вставки элемента: {self.__root} больше, чем {new_node}')
        except Exception as e:
            print(e)

    def get_right_child(self):
        try:
            return self.right_child
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')

    def get_left_child(self):
        try:
            return self.left_child
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')

    def get_root(self):
        try:
            return self.__root
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')


def test():
    tree1 = BinaryTree(8)
    print(tree1.get_root())
    print(tree1.get_left_child())
    tree1.insert_left(9)
    tree1.insert_left(1)
    print(tree1.get_left_child())
    print(tree1.get_left_child().get_root())
    tree1.insert_right(1)
    tree1.insert_right(12)
    print(tree1.get_right_child())
    print(tree1.get_right_child().get_root())


test()
