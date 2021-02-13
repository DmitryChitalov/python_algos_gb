"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""
class InvalidNode(Exception):
    pass

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
        #
        if new_node >= self.root:
            raise InvalidNode
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
        if new_node <= self.root:
            raise InvalidNode
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

    def print_tree(self, child = None, level=0, lr=''):
        if level == 0:
            print("Rt\'"+str(self.root))
            if self.right_child != None:
                self.print_tree(self.right_child, level + 1, 'R\'')
            if self.left_child != None:
                self.print_tree(self.left_child, level + 1, 'L\'')

        else:
            print("\t"*level+lr+str(child.root))
            if child.right_child != None:
                child.print_tree(child.right_child, level + 1, 'R\'')
            if child.left_child != None:
                child.print_tree(child.left_child, level + 1, 'L\'')



r = BinaryTree(8)
r.insert_left(4)
r.insert_right(12)

r.get_left_child().insert_left(2)
r.get_left_child().insert_right(6)
r.get_right_child().insert_left(10)
r.get_right_child().insert_right(14)

r.get_left_child().get_left_child().insert_left(1)
r.get_left_child().get_left_child().insert_right(3)

r.get_left_child().get_right_child().insert_left(5)
r.get_left_child().get_right_child().insert_right(7)

r.get_right_child().get_left_child().insert_left(9)
# для проверки ошибки
# r.get_right_child().get_left_child().insert_left(12)
r.get_right_child().get_left_child().insert_right(11)

r.get_right_child().get_right_child().insert_left(13)
r.get_right_child().get_right_child().insert_right(15)

r.print_tree()