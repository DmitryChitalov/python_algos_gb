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


class Tree:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(elements, tree_dict=dict(), code=''):
    if elements is None:
        return

    if isinstance(elements.value, str):
        tree_dict[elements.value] = code
        return tree_dict

    get_code(elements.left, tree_dict, code + '0')
    get_code(elements.right, tree_dict, code + '1')

    return tree_dict


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        tree = Tree(None)

        if len(string_count) == 1:
            tree.left = Tree([el for el in string_count][0])
            tree.right = Tree(None)

        string_count = {tree: 1}

    while len(string_count) != 1:
        tree = Tree(None)
        mst_cmmn = string_count.most_common()[:-3:-1]

        if isinstance(mst_cmmn[0][0], str):
            tree.left = Tree(mst_cmmn[0][0])

        else:
            tree.left = mst_cmmn[0][0]

        if isinstance(mst_cmmn[1][0], str):
            tree.right = Tree(mst_cmmn[1][0])

        else:
            tree.right = mst_cmmn[1][0]

        del string_count[mst_cmmn[0][0]]
        del string_count[mst_cmmn[1][0]]
        string_count[tree] = mst_cmmn[0][1] + mst_cmmn[1][1]

    return [el for el in string_count][0]


def encoding(string, encode):
    result = ''

    for elem in string:
        result += encode[elem]

    return result




string = 'beep boop beer!'
tree = get_tree(string)

code = get_code(tree)
print(f'Шифр: {code}')

coding = encoding(string, code)
print(f'Исходная строка: {string}')
print(f'Сжатая строка: {coding}')
