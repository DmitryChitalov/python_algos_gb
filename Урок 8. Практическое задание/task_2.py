"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class BinaryTree:
    def __init__(self, root_obj, data = None):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if self.root > new_node:
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
            else:
                print('Невозможно установить левого  с таким значением')
        except AttributeError:
            pass

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root <= new_node:
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
            else:
                print('Невозможно установить правого с таким значением')
        except AttributeError:
            pass

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            return self.right_child
        except AttributeError:
            print("Обьект не найден")

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            a = self.left_child
            return a
        except AttributeError:
            print("Обьект не найден")

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        try:
            a = self.root
            return a
        except AttributeError:
            print("Обьект не найден")

    # метод распечатки дерева
    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        print(self.get_root_val()),
        if self.right_child:
            self.right_child.print_tree()


if __name__ == '__main__':
    r = BinaryTree(8)
    # print(r.get_root_val())
    # print(r.get_left_child())
    # r.insert_left(12)
    r.insert_left(4)
    r.get_left_child().insert_left(2)
    # print(r.get_left_child().get_root_val())
    # print(r.get_left_child().get_left_child().get_root_val())
    # # r.insert_right(7)
    r.insert_right(12)
    # print(r.get_right_child())
    # print(r.get_right_child().get_root_val())
    # r.get_right_child().set_root_val(16)
    # print(r.get_right_child().get_root_val())
    # print(r.get_root_val())
    r.insert_right(16)
    # print(r.get_right_child())
    # print(r.get_right_child().get_root_val())
    r.print_tree()
