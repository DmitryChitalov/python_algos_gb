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

    def insert_node(self, data):
        # принимает данные и сразу раскидывает их вправо-влево в зависимости от их значения по отношению к корню
        if self.root:
            if data < self.root:
                if self.left_child is None:
                    self.left_child = BinaryTree(data)
                else:
                    self.left_child.insert_node(data)
            elif data > self.root:
                if self.right_child is None:
                    self.right_child = BinaryTree(data)
                else:
                    self.right_child.insert_node(data)
        else:
            self.root = data

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

    def PrintTree(self):
        if self.left_child:
            self.left_child.PrintTree()
        print( self.root),
        if self.right_child:
            self.right_child.PrintTree()


r = BinaryTree(8)
r.insert_node(14)
r.insert_node(65)
r.insert_node(31)
r.insert_node(3)
r.insert_node(19)

r.PrintTree()




