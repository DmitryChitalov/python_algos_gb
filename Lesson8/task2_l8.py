"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

# Надо сделать так, чтобы при вставке потомки сравнивались, и больший шел вправо, меньший - влево
# Я смогла сделать только так, чтобы больший потомок не вставлялся влево, и меньший - вправо.

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
         if self.left_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
         if new_node > self.root:    #условие на соблюдение старшинства
                raise Exception("Левый потомок должен быть меньше правого")
         else:
        # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        if new_node<self.root:             #условие на соблюдение старшинства
            raise Exception("Правый потомок должен быть больше левого")

        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
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


r = BinaryTree(14)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(15)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

# ПРАВИЛЬНОЕ РЕШЕНИЕ ИЗ ВЫЛОЖЕННЫХ К ДЕДЛАЙНУ:

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node [{str(self.value)}]'


class Tree:
    def __init__(self):
        self.root = None

    # функция для добавления узла в дерево
    def new_node(self, data):
        temp = Node(0, None, None)
        temp.data = data
        return temp

    # функция для вычисления высоты дерева
    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return (lheight + 1)
            else:
                return (rheight + 1)

    # функция для распечатки элементов на определенном уровне дерева
    def print_given_level(self, root, level, ltr):
        if root == None:
            return
        if level == 1:
            print("%d " % root.data)
        elif level > 1:
            if ltr:
                self.print_given_level(root.left, level - 1, ltr);
                self.print_given_level(root.right, level - 1, ltr);
            else:
                self.print_given_level(root.right, level - 1, ltr);
                self.print_given_level(root.left, level - 1, ltr);

    # функция для распечатки дерева
    def print_level_order(self, root):
        h = self.height(self.root)
        i = 1
        ltr = 1
        while i <= h:
            self.print_given_level(self.root, i, ltr)
            i += 1

    # функция для вычисления ширины дерева
    def get_max_width(self, root):
        max_wdth = 0
        i = 1
        width = 0
        h = self.height(root)
        while i < h:
            width = self.get_width(root, i)
            if width > max_wdth:
                max_wdth = width
            i += 1

        return max_wdth

    def get_width(self, root, level):
        if root == None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.get_width(root.left, level - 1) + self.get_width(root.right, level - 1)
        self.get_width(root.right, level - 1)


t = Tree()
t.root = t.new_node(8)

t.root.left = t.new_node(4)
t.root.right = t.new_node(12)
t.root.left.left = t.new_node(2)
t.root.left.right = t.new_node(6)
t.root.right.left = t.new_node(10)
t.root.right.right = t.new_node(14)
t.root.left.left.left = t.new_node(1)
t.root.right.right.right = t.new_node(25)
t.root.left.left.left.left = t.new_node(0)
t.root.left.left.right = t.new_node(3)
t.root.right.right.right.right = t.new_node(100)
t.root.right.right.right.left = t.new_node(20)

t.print_level_order(t.root)
print(f'Высота: {t.height(t.root)}')
print(f'Ширина: {t.get_max_width(t.root)}')

# Я, возможно не разобралась, но мне показалось, что в такой конфигурации можно вставить бОльшего потомка влево.
