"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""
"""Добавил функцию для валидации требований к структуре бинарного дерева и функцию для определения высоты дерева"""


class NodeValueError(Exception):
    def __init__(self, warning_text):
        """Генерирует предупреждающее сообщение, если нарушена логика дерева при вставке нового узла"""
        self.txt = warning_text


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def validate_left(self, new_node):
        if self.left_child == None and self.get_root_val() > new_node:
            return True
        elif self.left_child == None and self.get_root_val() < new_node:
            print('hi')
            raise NodeValueError('Значение левого потомка должно быть меньше значения родителя')
        elif self.get_left_child().get_root_val() > new_node:
            return True
        raise NodeValueError('Значение левого потомка должно быть меньше значения родителя')

    def validate_right(self, new_node):
        if self.right_child == None and self.get_root_val() < new_node:
            return True
        elif self.right_child == None and self.get_root_val() > new_node:
            raise NodeValueError('Значение правого потомка должно быть больше значения родителя')
        elif self.get_right_child().get_root_val() < new_node:
            return True
        raise NodeValueError('Значение правого потомка должно быть больше значения родителя')

    # добавить левого потомка
    def insert_left(self, new_node):
        if self.validate_left(new_node):
            # если у узла нет левого потомка
            if self.left_child == None:
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

    # добавить правого потомка
    def insert_right(self, new_node):
        if self.validate_right(new_node):
            # если у узла нет правого потомка
            if self.right_child == None:
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

    # вычислить высоту дерева
    def height(self, node):
        if node is None:
            return -1
        else:
            left_height = self.height(node.get_left_child())
            right_height = self.height(node.get_right_child())
            return 1 + max(left_height, right_height)


try:
    r = BinaryTree(8)
    print(f'Высота бинарного дерева: {r.height(r)}')  # если дерево имеет только корень (потомков нет), его высота = 0
    print(r.get_root_val())
    print(r.get_left_child())
    #  пробуем вставить левого потомка со значением больше значения родителя, получаем исключение
    #  r.insert_left(9)
    r.insert_left(4)
    print(f'Высота бинарного дерева: {r.height(r)}')  # корень имеет одного потомка, высота = 1
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    #  пробуем вставить правого потомка со значением меньше значения родителя, получаем исключение
    #  r.insert_right(7)
    r.insert_right(12)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(16)
    print(r.get_right_child().get_root_val())
    print(r.get_left_child().get_root_val())
    r.insert_left(3)
    print(r.get_left_child().get_root_val())
    #  пробуем вставить левого потомка со значением больше значения родителя, получаем исключение
    # r.insert_left(5)
    print(r.get_right_child().get_root_val())
    #  пробуем вставить правого потомка со значением меньше значения родителя, получаем исключение
    # r.insert_right(15)
    print(f'Высота бинарного дерева: {r.height(r)}')
    r.insert_left(1)
    print(f'Высота бинарного дерева: {r.height(r)}')
except NodeValueError as error:
    print(error)
