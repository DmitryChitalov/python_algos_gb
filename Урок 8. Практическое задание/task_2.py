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

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # и узел меньше корня
            if new_node < self.get_root_val():
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            else:
                # если новый узел больше корня:
                raise ValueError(f'Введите число меньше корня. Корень: {self.get_root_val()}')

        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # если новый узел меньше корня
            if new_node < self.get_root_val():
                # и больше имеющегося потомка
                if new_node > self.left_child.get_root_val():
                    # тогда спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
                else:
                    # если узел меньше имеющегося потомка:
                    raise ValueError('Проверьте есть ли у потомка свой левый потомок.')
            else:
                # если новый узел больше корня:
                raise ValueError(f'Введите число меньше корня. Корень: {self.get_root_val()}')

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # и правый потомок больше корня
            if new_node > self.get_root_val():
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            else:
                # если новый узел меньше корня:
                raise ValueError(f'Введите число больше корня. Корень: {self.get_root_val()}')
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # если новый узел больше корня
            if new_node > self.get_root_val():
                # и меньше имеющегося потомка
                if new_node < self.right_child.get_root_val():
                    # тогда спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                else:
                    # если узел больше имеющегося потомка:
                    raise ValueError('Проверьте есть ли у потомка свой правый потомок.')
            else:
                # если новый узел меньше корня:
                raise ValueError(f'Введите число больше корня. Корень: {self.get_root_val()}')

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

# r.insert_left(10)                     # ValueError: Введите число меньше корня. Корень: 8
r.insert_left(4)
# r.insert_left(2)                      # ValueError: Проверьте есть ли у потомка свой левый потомок.

print(r.get_left_child())
print(r.get_left_child().get_root_val())

# r.insert_right(6)                     # ValueError: Введите число больше корня. Корень: 8
r.insert_right(12)
# r.insert_right(14)                    # ValueError: Проверьте есть ли у потомка свой правый потомок.

print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

"""
Была добавлена валидация значений в зависимости от того, какой потомок вставляется: 
Если левый, то проводится сравнение нового узла с корнем (новый узел должен быть меньше корня). Также проводится
сравнение нового узла с имеющимся левым потомком. Если новый узел больше имеющегося левого потомка, то имеющийся
потомок спускается на уровень ниже, если же меньше, то вставка не происходит и выводится ошибка, что необходимо 
проверить есть ли у потомка свой правый потомок.
"""