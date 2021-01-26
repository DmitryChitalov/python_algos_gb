"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
from collections import Counter


test_string = "abracadabra"


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class Tree:
    def __init__(self, chars):
        self.chars = Counter(chars)

    def make_tree(self):
        tree = self.chars.items()
        while len(tree) > 1:
            tree = sorted(tree, reverse=True, key=lambda i: i[1])
            char1, count1 = tree.pop()
            char2, count2 = tree.pop()
            tree.append(
                (Node(char1, char2), count1 + count2)
            )
        return tree[0][0]


def haffman_tree(node, code=""):
    if type(node) is str:
        return {node: code}
    result = {}
    result.update(haffman_tree(node.left, code + "0"))
    result.update(haffman_tree(node.right, code + "1"))
    return result


tree = Tree(test_string)
char_tree = haffman_tree(tree.make_tree())

print(char_tree)
