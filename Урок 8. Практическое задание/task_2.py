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
        #Левый потомок всегда меньше
        if new_node < self.root:
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
        else: print(f'Вы ввели число больше корня воспользуйтесь insert_right')
    # добавить правого потомка
    def insert_right(self, new_node):
        #Правый потомок всегда больше
        if new_node > self.root:
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
        else: print(f'Вы ввели число меньше корня воспользуйтесь insert_left')
    # метод доступа к правому потомку
    def get_right_child(self):
        if self.right_child != None:
            return self.right_child
        else:
            return 'Правая ветка пуста'
    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child != None:
            return self.left_child
        else:
            return 'Левая ветка пуста'

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def get_left(self):
        try:
            return r.get_left_child().get_root_val()
        except AttributeError:
            return 'Левая ветка пуста'

    def get_right(self):
        try:
            return r.get_right_child().get_root_val()
        except AttributeError:
            return 'Правая ветка пуста'

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

"""
Сделана проверка на добавление левого и правого потомка,
согласно условию бинрного дерева, левый потомк меньше корня, правый больше
Реализовано Try except
"""