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

    # функция для вычисления высоты дерева
    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left_child)
            rheight = self.height(node.right_child)

            if lheight > rheight:
                return (lheight + 1)
            else:
                return (rheight + 1)

    # функция для распечатки элементов на определенном уровне дерева
    def printGivenLevel(self, root, level, direct):
        if root == None:
            return
        if level == 1:
            print(f" {direct} : {root.root}")
        elif level > 1:
            self.printGivenLevel(root.left_child, level - 1, "лево");
            self.printGivenLevel(root.right_child, level - 1, "право");

    # функция для распечатки дерева
    def printLevelOrder(self):
        h = self.height(self)
        i = 1
        while (i <= h):
            self.printGivenLevel(self, i, "начало")
            i += 1

    # функция для проверки наличия узла
    def lookup(self, node, target):
        if node == None:
            return 'Нет'
        else:
            if target == node.root:
                return 'Есть'
            else:
                if target < node.root:
                    return self.lookup(node.left_child, target)
                else:
                    return self.lookup(node.right_child, target)


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print("Отображение:")
r.printLevelOrder()
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
r.insert_right(7)
print(r.get_right_child().insert_right(32))

print("Проверка наличия узла:", r.lookup(r, 7))
print("Проверка наличия узла:", r.lookup(r, 8))
print("Высота:", r.height(r))
print("Отображение:")
r.printLevelOrder()

