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

        # Количество подуровней
        self.lvl_count = [0, 0]

    # Добавляем потомка
    def insert(self, new_node):
        """
        Метод, который решает в какую сторону добавлять элементы
        """
        if new_node == self.root:
            print('Данное значение в бинарном дереве уже есть!')
        elif new_node < self.root:
            self.__insert_left(new_node)
        else:
            self.__insert_right(new_node)

    # добавить левого потомка
    def __insert_left(self, new_node):
        """
        Изменил способ добавления значений узлам.
        """
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
            self.lvl_count[0] = 1
        # если у узла есть левый потомок
        else:
            # Тогда отправляем левому потомку новое значение на его откуп
            self.left_child.insert(new_node)
            self.lvl_count[0] = max(self.left_child.lvl_count) + 1

    # добавить правого потомка
    def __insert_right(self, new_node):
        """
        Изменил способ добавления значений узлам.
        """
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
            self.lvl_count[1] = 1
        # если у узла есть правый потомок
        else:
            # Тогда отправляем правому потомку новое значение на его откуп
            self.right_child.insert(new_node)
            self.lvl_count[1] = max(self.right_child.lvl_count) + 1

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def print_tree(self):
        for i in range(max(self.lvl_count) + 1):
            self.print_lvl(i)
            print()
        print()

    def print_lvl(self, lvl=0):
        if lvl == 0:
            print(self.root, end='\t')
            return
        if lvl <= self.lvl_count[0]:
            self.left_child.print_lvl(lvl - 1)
        if lvl <= self.lvl_count[1]:
            self.right_child.print_lvl(lvl - 1)


r = BinaryTree(8)
r.print_tree()

r.insert(4)
r.print_tree()

r.insert(2)
r.print_tree()

r.insert(10)
r.print_tree()

r.insert(6)
r.print_tree()

r.insert(6)
r.print_tree()

r.insert(12)
r.print_tree()

r.insert(9)
r.print_tree()

r.insert(7)
r.print_tree()

print(r.get_left_child().get_root_val())
print(r.get_left_child().get_left_child().get_root_val())


# r.insert_left(10)
# print(r.get_left_child())
# r.insert_left(4)
# print(r.get_left_child())
# print(r.get_left_child().get_root_val())
# r.insert_right(12)
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val(16)
# print(r.get_right_child().get_root_val())
