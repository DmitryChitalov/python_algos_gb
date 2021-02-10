"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

"""
Сделал валидацию узлов.
Левый узел должен быть всегда меньше корня, правый узел - больше корня.
При введении неверного числа - требуется ввести верное число до тех пор, пока оно не будет введено.
Верное число запоминается как new_node и используется дальше функцией.
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # Валидация левого узла
        self.new_node = new_node
        while self.new_node > self.root:
            self.new_node = int(input(f"Левый узел должен быть меньше {self.root}: "))

        if self.new_node < self.root:
            # если у узла нет левого потомка
            if self.left_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(self.new_node)
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(self.new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # Валидация правого узла
        self.new_node = new_node
        while self.new_node < self.root:
            self.new_node = int(input(f"Правый узел должен быть больше {self.root}: "))

        if self.new_node > self.root:
            # если у узла нет правого потомка
            if self.right_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(self.new_node)

            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(self.new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj

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
r.insert_left(9)
print('left_child = ', r.get_left_child().get_root_val())
r.insert_right(5)
print('right_child = ', r.get_right_child().get_root_val())
