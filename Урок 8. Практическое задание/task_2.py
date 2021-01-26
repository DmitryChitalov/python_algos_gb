"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

"""
Доработки:
1. Изменена функция insert, которая проверяет величину вставляемого значения и сама определяет его как левого или
правого потомка.
2. Для проверки дерева добавлена функция распечатки дерева (каждый уровень - отдельная строка). Для ее реализации
добавлены функции:
3. вспомогательная функция tree_to_list для преобразования дерева в список
4. вспомогательная функция get_depth для определения количества уровней дерева
"""


class BinaryTree:
    def __init__(self, data):
        self.data = data
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left_child is None:
                    self.left_child = BinaryTree(data)
                else:
                    self.left_child.insert(data)
            elif data >= self.data:
                if self.right_child is None:
                    self.right_child = BinaryTree(data)
                else:
                    self.right_child.insert(data)
        else:
            self.data = data



                    # # добавить левого потомка
    # def insert_left(self, new_node):
    #     # если у узла нет левого потомка
    #     if self.left_child == None:
    #         # тогда узел просто вставляется в дерево
    #         # формируется новое поддерево
    #         self.left_child = BinaryTree(new_node)
    #     # если у узла есть левый потомок
    #     else:
    #         # тогда вставляем новый узел
    #         tree_obj = BinaryTree(new_node)
    #         # и спускаем имеющегося потомка на один уровень ниже
    #         tree_obj.left_child = self.left_child
    #         self.left_child = tree_obj
    #
    # # добавить правого потомка
    # def insert_right(self, new_node):
    #     # если у узла нет правого потомка
    #     if self.right_child == None:
    #         # тогда узел просто вставляется в дерево
    #         # формируется новое поддерево
    #         self.right_child = BinaryTree(new_node)
    #     # если у узла есть правый потомок
    #     else:
    #         # тогда вставляем новый узел
    #         tree_obj = BinaryTree(new_node)
    #         # и спускаем имеющегося потомка на один уровень ниже
    #         tree_obj.right_child = self.right_child
    #         self.right_child = tree_obj


    # метод доступа к правому потомку

    def get_right_child(self):
         if self.right_child is None:
            return BinaryTree(None)
         else:
            return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
         if self.left_child is None:
            return BinaryTree(None)
         else:
            return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.data

    # вспомогательная функция определения количества уровней дерева
    def get_depth(self):
        if self.data is None:
            return 0
        else:
            return 1 + max(self.get_left_child().get_depth(), self.get_right_child().get_depth());

    # вспомогательная функция для преобразования дерева в список
    def tree_to_list(self, lst, depth, level=0):
        if len(lst) <= level:
            lst.append([])
        if lst[level] is None:
            lst[level] = [self.data]
        else:
            lst[level].append(self.data)

        if level + 1 >= depth:
            return
        left = self.get_left_child()
        if left is not None:
            left.tree_to_list(lst, depth, level + 1)

        right = self.get_right_child()
        if right is not None:
            right.tree_to_list(lst, depth, level + 1)

    # распечатывание дерева
    def print(self):
        lst = []
        r.tree_to_list(lst, r.get_depth())
        for row in lst:
            print(row)

r = BinaryTree(8)
print(r.get_left_child())

r.insert(4)
r.insert(2)
r.insert(20)
r.insert(10)
r.insert(21)
r.insert(22)

print(r.get_left_child().get_root_val())

lst = []
r.tree_to_list(lst, r.get_depth())
print(lst)
print(r.get_depth())
r.print()

