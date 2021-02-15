"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def insert_node(self, new_node):
        if self.root <= new_node:
            self.__insert_right(new_node)
        else:
            self.__insert_left(new_node)

    # добавить левого потомка
    def __insert_left(self, new_node):
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
    def __insert_right(self, new_node):
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
    def __set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_node(40)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.insert_node(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
print(r.get_right_child().get_right_child().get_root_val())
# r.get_right_child().set_root_val(16)
r.insert_node(11)
print(r.get_right_child().get_root_val())
print(r.get_right_child().get_right_child().get_root_val())
r.insert_node(7)
print(r.get_left_child().get_root_val())

"""
Моя небольшая доработка следующая. Замена пользовательских функций добавления 
левого и правого потомков на одну insert_node().
insert_left и insert_right сделаны приватными и вызываются из insert_node() в 
зависимости от того больше или меньше добавляемый узел чем вершина.
Это позволяет исключить риски некорректного заполнения пользователем бинарного дерева.
"""
