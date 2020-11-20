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


def code_haffman_tree(input_string):
    letters = Counter(input_string)
    trees = [BinaryTree(x[0], x[1]) for x in letters.items()]
    items = sorted(trees, key=lambda item: item.weight)

    while len(items) > 1:

        tree = BinaryTree(None, 0)
        tree.set_left_child(items.pop(0))
        tree.set_right_child(items.pop(0))
        weight = tree.get_weight()

        for i in range(len(items)):
            current_weight = items[i].get_weight()
            if weight <= current_weight:
                items.insert(i, tree)
                break
        else:
            items.insert(len(items), tree)
    return items[0]


def get_haffman_table(tree, path=''):
    if tree.name is not None:
        code_table[tree.name] = path
    else:
        get_haffman_table(tree.get_left_child(), path=f'{path}0')
        get_haffman_table(tree.get_right_child(), path=f'{path}1')


class BinaryTree:
    def __init__(self, name, weight):
        self.childs = {"0": None, "1": None}
        self.name = name
        self.weight = weight

    def set_left_child(self, child):
        self.childs["0"] = child

    def set_right_child(self, child):
        self.childs["1"] = child

    def get_left_child(self):
        return self.childs["0"]

    def get_right_child(self):
        return self.childs["1"]

    def get_weight(self):
        if (self.childs["0"] is not None) & (self.childs["1"] is not None):
            return self.childs["0"].get_weight() + self.childs["1"].get_weight()
        elif self.childs["0"] is not None:
            return self.childs["0"].get_weight()
        elif self.childs["1"] is not None:
            return self.childs["1"].get_weight()
        else:
            return self.weight

    def is_end_element(self):
        return (self.childs["0"] is not None) & (self.childs["1"] is not None)

    def __str__(self):
        return f"{self.name} - {self.weight}"


code_table = dict()
haffman_tree = code_haffman_tree("beep boop beer!")
get_haffman_table(haffman_tree)
print(code_table)
"{'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}"
