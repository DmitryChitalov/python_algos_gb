"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


def error_type(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as deus:
            print(deus)
        except AttributeError:
            print('Ошибка доступа к атрибуту класса')

    return wrapper


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def __str__(self):
        return str(self.root)

    @error_type
    def insert_left(self, new_node):
        if new_node < self.root:  # значения слева должно быть меньше
            # если у узла нет левого потомка
            if self.left_child == None:
                self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        else:
            raise Exception('Ошибка вставки!')

    # добавить правого потомка

    @error_type
    def insert_right(self, new_node):
        if new_node >= self.root:  # значения справа должно быть равно и больше
            # если у узла нет правого потомка
            if self.right_child == None:
                self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
            else:
                tree_obj = BinaryTree(new_node)
            # спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        else:
            raise Exception('Ошибка вставки')

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
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
