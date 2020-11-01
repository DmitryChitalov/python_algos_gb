"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class BinaryTree:
    def __init__(self, root, left=None, right=None, level=1):
        self.root = root
        self.left = left
        self.right = right
        self.level = level

    def add_to_left_new_branch(self):
        """
        Делаем из левой ветки корень, инициируем класс. Левое значение становится корнем для нового дерева
        """
        self.left = BinaryTree(self.left, level=self.level+1)

    def add_to_right_new_branch(self):
        """
        Делаем из правой ветки корень, инициируем класс. Правое значение становится корнем для нового дерева
        """
        self.right = BinaryTree(self.right, level=self.level+1)

    def add_left_value(self, left):
        """
        Изменяем левое значение, даже если "лево" это "дерево", то меняем корень
        """
        if isinstance(self.left, BinaryTree):
            self.left.root = left
            print(f'На уровне {self.level} изменено левое значение на ', left)
        else:
            self.left = left
            print(f'На уровне {self.level} изменено левое значение на ', left)

    def add_right_value(self, right):
        """
        Изменяем правое значение, даже если "право" это "дерево", то меняем корень
        """
        if isinstance(self.right, BinaryTree):
            self.right.root = right
            print(f'На уровне {self.level} изменено правое значение на ', right)
        else:
            self.right = right
            print(f'На уровне {self.level} изменено правое значение на ', right)

    def add_value_way(self, value, way):
        """
        С помощью бинарного пути добавляем заначени на определённое место
        """
        if len(way) > 1:
            if int(way[0]):
                try:
                    self.right.add_value_way(value, way[1:])
                except AttributeError:  # отлавливаем ошибку, если путь длинее дерева
                    self.add_to_right_new_branch()
                    self.right.add_value_way(value, way[1:])
            else:
                try:
                    self.left.add_value_way(value, way[1:])
                except AttributeError:  # отлавливаем ошибку, если путь длинее дерева
                    self.add_to_left_new_branch()
                    self.left.add_value_way(value, way[1:])
        else:
            if int(way):
                self.add_right_value(value)
            else:
                self.add_left_value(value)

    def __str__(self):
        return f'level-{self.level}\n (root-{self.root} left-{self.left}|right-{self.right})'


if __name__ == '__main__':
    tree = BinaryTree(8)
    tree.add_left_value(6)
    tree.add_right_value(11)
    tree.add_to_right_new_branch()
    tree.add_to_left_new_branch()
    tree.add_value_way(5, '00')
    tree.add_value_way(7, '01')
    tree.add_value_way(9, '10')
    tree.add_value_way(12, '11')
    tree.add_right_value(10)    # заменяем значение заданное на 85 строчке
    tree.add_value_way(11, '110')
    tree.add_value_way(13, '111')
    tree.add_value_way(55, '0101')
    print(tree)
