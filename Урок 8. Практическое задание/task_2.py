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
        print(f'++ {root_obj} is set as a "Root"')
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        """
            Функция добавляет элемент в левую ветвь дерева.
            Добавлена проверка: элемент добавляется в дерево только если
            его значение меньше "корневого элемента".
        """
        if new_node < self.root:
            # если у узла нет левого потомка
            print(f'+ New child "{new_node}" has added into left branch.')
            if self.left_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        elif new_node == self.root:
            print('== Error! Values "root" and "child" are equal.')
        else:
            print('>> Error! The "node" is too large to insert into left branch!')

    # добавить правого потомка
    def insert_right(self, new_node):
        """
            Функция добавляет элемент в правую ветвь дерева.
            Добавлена проверка: элемент добавляется в дерево только если
            его значение больше "корневого элемента".
        """
        if new_node > self.root:
            # если у узла нет правого потомка
            print(f'New child "{new_node}" has added into right branch.')
            if self.right_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        elif new_node == self.root:
            print('== Error! Values "node" and "child" are equal.')
        else:
            print('<< Error! The "node" is too small to insert into right branch!')

    # метод доступа к правому потомку
    def get_right_child(self):
        if self.right_child is None:
            return 'Right branch is empty now!'
        else:
            return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child is None:
            return 'Left branch is empty now!'
        else:
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
r.insert_left(6)
r.insert_left(8)
print(f'Check root value — {r.get_root_val()}')
r.insert_left(100)
r.insert_left(1)
print(r.get_left_child())
print(r.get_right_child())
r.insert_right(12)
r.insert_right(2)
r.insert_right(26)
r.insert_right(8)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
