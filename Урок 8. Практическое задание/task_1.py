"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
"""
Реализация при помощи дерева
"""
from collections import Counter


class Node:
    def __init__(self, weight=0, value=None, left=None, right=None):
        self.weight = weight
        self.value = value
        self.left = left
        self.right = right
        self.code = ''

    def add(self, value, weight):
        if self.left is None:
            self.left = Node(self, weight, value)
            self.weight = self.left.weight
            self.code = '0'
        else:
            self.right = Node(self, weight, value)
            self.weight = self.left.weight + self.right.weight
            self.code = '1'
        self.value = None


def get_code(node, in_char):
    if node.value == in_char: return node.code
    t_code = ''
    if not node.left is None:
        t_code = get_code(node.left, in_char)
    if t_code == '' and not node.right is None:
        t_code = get_code(node.right, in_char)
    if t_code != '': t_code = str(t_code) + str(node.code)
    return t_code


def print_tree(node):
    if not node.left is None:
        print_tree(node.left)
    if not node.right is None:
        print_tree(node.right)
    if node.left is None and node.right is None: print(node.value)


s = 'asdfge ! df sh   33resdfw efwefsd'
count = Counter(s)
print(count)
sorted_arr = sorted(count.items(), key=lambda item: item[1])
print(sorted_arr)

index = 0
nodes = []
for i in range(len(sorted_arr)):
    nodes.append(Node(sorted_arr[i][1], sorted_arr[i][0]))

while (len(nodes) > 1):
    nodes = sorted(nodes, key=lambda nd: nd.weight)
    left = nodes[0]
    right = nodes[1]

    left.code = 0
    right.code = 1

    newNode = Node(left.weight + right.weight, left.value + right.value, left, right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

print_tree(nodes[0])
print(f'String <{s}>')
for i in range(len(s)):
    print(f'Char {s[i]} code {get_code(nodes[0], s[i])}')
