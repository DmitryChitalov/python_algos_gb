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


sample = 'Кодирование по Хаффману через ООП.'
print("Исходная строка: ", sample)


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def child(self):
        return self.left, self.right


def haffman_tree(node, code=""):
    if type(node) is str:
        return {
            node: code
        }

    l, r = node.child()

    result = {}

    result.update(haffman_tree(l, code + "0"))
    result.update(haffman_tree(r, code + "1"))

    return result


frequencies = {}
for char in sample:
    if char not in frequencies:
        frequencies[char] = 0

    frequencies[char] += 1

tree = frequencies.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append(
        (Node(char1, char2), count1 + count2)
    )

table = haffman_tree(tree[0][0])

coded = []
for char in sample:
    coded.append(table[char])

print("Закодированная строка: ", "".join(coded))
