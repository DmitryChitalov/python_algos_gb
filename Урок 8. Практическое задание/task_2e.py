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
        # тогда узел просто вставляется в дерево
        # формируется новое поддерево
        if self.left_child == None:
            # у двоичного дерева поиска значение левого узла всегда меньше или равно значению правого узла
            if new_node > self.root:
                raise Exception('Значение левого узла больше значения корня!')
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        # тогда вставляем новый узел
        # и спускаем имеющегося потомка на один уровень ниже
        else:
            # у двоичного дерева поиска значение левого узла всегда меньше или равно значению правого узла
            if new_node < self.left_child.get_root_val():
                raise Exception('Значение левого узла больше значения корня!')
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):

        # если у узла нет правого потомка
        # тогда узел просто вставляется в дерево
        # формируется новое поддерево
        if self.right_child == None:
            # у двоичного дерева поиска значение правого узла всегда больше или равно значению корня
            if new_node < self.root:
                raise Exception('Значение правого узла меньше значения корня!')
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        # тогда вставляем новый узел
        # и спускаем имеющегося потомка на один уровень ниже
        else:
            # у двоичного дерева поиска значение правого узла всегда больше или равно значению корня
            if new_node < self.right_child.get_root_val():
                raise Exception('Значение правого узла меньше значения корня!')
            tree_obj = BinaryTree(new_node)
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
print(r.get_left_child())
r.insert_left(4)
# r.insert_left(2) - здесь генерится ошибка
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
r.insert_right(13)
# r.insert_right(11) - здесь генерится ошибка
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())


"""
В данном задании я добавил проверку значения узлов дерева поиска: 
    1) если значение левого узла больше значения корня - генерить ошибку
    2) если значение правого узла меньше значения корня - генерить ошибку
Также прогнал разные варианты добавления элементов в дерево.
"""