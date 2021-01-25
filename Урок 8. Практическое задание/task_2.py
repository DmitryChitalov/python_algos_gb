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
        if new_node < self.root:
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
        else:
            raise Exception('The left child cannot be larger than the root')


    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if new_node > self.root:
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
        else:
            raise Exception('The right child cannot be less than the root')

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


r = BinaryTree(10)
print(r.get_root_val())

r.insert_left(5)
r.get_left_child().insert_left(2)
r.get_left_child().insert_right(7)

print(r.get_left_child().get_left_child().get_root_val())
print(r.get_right_child())
r.insert_right(15)
r.get_right_child().insert_left(12)
r.get_right_child().insert_right(17)
print(r.get_root_val())
print(r.get_right_child().get_left_child().get_root_val())
r.get_right_child().get_left_child().insert_left(8) # -- вот тут вопрос, может быть так?

"""
возможно ли такое дерево:
           10
        |       |
        5      15
      |  |    |   |
      2  7    8   17

Вопрос про 8, если да то все ок
если нет, то получается потомков нужно проверять дальше, с основным корнем
"""


