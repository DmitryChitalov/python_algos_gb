"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями
для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""
from random import randint


class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f'{self.key}'


class BinaryTree:

    def __init__(self):
        self.root = None

    def __str__(self):
        return self.show_tree(self.root)

    # метод выстраивает порядок элементов дерева слева направо
    def show_tree(self, node):
        if node is None:
            return 'Нет такого ключа в дереве'
        if node.left is None and node.right is None:
            return f'{node.key}'
        if node.left is None:
            return f'{node.key} {self.show_tree(node.right)}'
        if node.right is None:
            return f'{self.show_tree(node.left)} {node.key}'
        return f'{self.show_tree(node.left)} {node.key} ' \
               f'{self.show_tree(node.right)}'

    # поиск по дереву
    def find(self, data):
        p = self.root
        while p is not None and p.key != data:
            if data < p.key:
                p = p.left
            else:
                p = p.right
        return p

    # добавление элемента в структуру дерева
    def insert(self, data):
        if isinstance(data, Node):
            data = data.key
        p = self.find(data)
        if p is not None:
            return
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        p = self.root
        while True:
            if data < p.key:
                if p.left is None:
                    p.left = node
                    node.parent = p
                    return
                else:
                    p = p.left
            else:
                if p.right is None:
                    p.right = node
                    node.parent = p
                    return
                else:
                    p = p.right


# создание дерева
new_tree = BinaryTree()

# добавление ключей в дерево
for i in range(10):
    new_tree.insert(randint(-100, 100))
    print(new_tree)

# поиск ключа в дереве
b = new_tree.find(31)
print(b)

# попытка напечатать дерево, начиная с найденного элемента
print(new_tree.show_tree(b))

# добавление ключа в дерево путем добавления готового узла
new_node = Node(67)
print(new_node)
# noinspection PyTypeChecker
new_tree.insert(new_node)
print(new_tree)

# поиск ключа в дереве
c = new_tree.find(67)
print(c)

# добавление ключей в дерево
for i in range(6):
    new_tree.insert(randint(50, 100))
    print(new_tree)

# попытка напечатать дерево, начиная с найденного элемента
print(new_tree.show_tree(c))

"""
Мне пришлось очень сильно изменить изначальный класс, потому что в 
тот код, который был, у меня не получалось внести изменения так, чтобы они 
соответствовали определению "бинарное дерево поиска"

В этом варианте отсутствует метод удаления узлов дерева, также можно написать 
методы, которые бы выводили левую или правую ветвь, начиная с конткретного 
узла и др.

Также, возможно, стоит написать метод, который выводил бы на печать структуру 
дерева построчно, например для дерева с элементами 8, 3, 1, 2, 10, 4, 6:
8
3 10
1 4 6
2

Также это дерево не сбалансировано, но чтобы его сбалансировать, придётся 
очень сильно менять код, у меня не хватит на это времени - очень медленно 
получается писать код, так как многое непонятно.

В целом в это дерево можно добавлять числа, и они автоматически будут 
расположены в нужном порядке. По этому дереву можно производить поиск
"""
