"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

from collections import deque

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        self.all_right_nodes = []
        self.all_left_nodes = []

    # добавить левого потомка
    def insert_left(self, new_node):
        # если узел должен быть справа
        if new_node > self.root:
            self.insert_right(new_node)
        # если у узла нет левого потомка
        elif not self.left_child:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
            self.all_left_nodes.append(self.left_child)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            for index, node in enumerate(self.all_left_nodes):
                if new_node > node.root:
                    if index == 0:
                        tree_obj.left_child = node
                        self.left_child = tree_obj
                        self.all_left_nodes.insert(index, tree_obj)
                        break
                    else:
                        tree_obj.left_child = node
                        self.all_left_nodes.insert(index, tree_obj)
                        break
                elif node is self.all_left_nodes[-1]:
                    self.all_left_nodes[len(self.all_left_nodes) - 1].left_child = tree_obj.root
                    self.all_left_nodes.append(tree_obj)
                    break

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            self.insert_left(new_node)
        # если у узла нет правого потомка
        elif not self.right_child:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
            self.all_right_nodes.append(self.right_child)
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            for index, node in enumerate(self.all_right_nodes):
                if new_node < node.root:
                    if index == 0:
                        tree_obj.right_child = node
                        self.right_child = tree_obj
                        self.all_right_nodes.insert(index, tree_obj)
                        break
                    else:
                        tree_obj.right_child = self.all_right_nodes[index]
                        self.all_right_nodes[index - 1].right_child = tree_obj
                        self.all_right_nodes.insert(index, tree_obj)

                        break
                elif node is self.all_right_nodes[-1]:
                    self.all_right_nodes[len(self.all_right_nodes) - 1].right_child = tree_obj.root
                    self.all_right_nodes.append(tree_obj)
                    break

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        if obj == self.root:
            pass
        elif obj > self.root:
            # self.root = obj
            for index, node in enumerate(self.all_right_nodes):
                if obj < node.root:
                    self.root = obj
                    self.right_child = node

                    for x in range(index):
                        self.all_left_nodes.insert(0, self.all_right_nodes[x])
                        self.all_left_nodes[0].left_child = self.all_left_nodes[1]
                        self.all_left_nodes[0].right_child = None

                    self.left_child = self.all_left_nodes[0]
                    self.all_right_nodes = self.all_right_nodes[index:]
                    break
        else:
            for index, node in enumerate(self.all_left_nodes):
                if obj > node.root:
                    self.root = obj
                    self.left_child = node

                    for x in range(index):
                        self.all_right_nodes.insert(0, self.all_left_nodes[x])
                        self.all_right_nodes[0].left_child = None

                    self.right_child = self.all_right_nodes[0]
                    self.all_left_nodes = self.all_left_nodes[index:]
                    break

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())

r.insert_left(40)
r.insert_left(4)
r.insert_left(-2)
r.insert_left(6)
print(r.all_left_nodes)
for i in r.all_left_nodes:
    print(i.root, end=" ")
print("\n")
print(r.left_child.root)

r.insert_right(20)
r.insert_right(16)
r.insert_right(24)
print(r.all_right_nodes)
for i in r.all_right_nodes:
    print(i.root)

print("Меняю значение главного узла на 22")
r.set_root_val(22)

for node in r.all_right_nodes:
    print("Я правый",node.root)
for node in r.all_left_nodes:
    print("Я левый", node.root)
print(f"Первый левый {r.left_child.root}")
print(f"Первый правый {r.right_child.root}")

print("Меняю значение главного узла на 8")
r.set_root_val(8)

for node in r.all_right_nodes:
    print("Я правый",node.root)
for node in r.all_left_nodes:
    print("Я левый", node.root)
print(f"Первый левый {r.left_child.root}")
print(f"Первый правый {r.right_child.root}")

"""
Добавил валидацию при вставках справа и слева неподоходящих значений, 
а также реформат при замене значения главного узла
"""