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
from collections import deque, Counter


class HuffmanTree:

    def __init__(self):
        self.string = self.get_string()
        self.sorted_string = self.sorting()
        self.sorted_string_reserve = self.sorted_string.copy()
        self.tree = self.create_tree()
        self._temp_tree = self.tree[0].copy()
        self._code = ''
        self._tab = {}
        self.tab = self.create_tab()

    def get_string(self):
        return input('Введите строку: ')

    def sorting(self):
        res = deque(sorted(Counter(self.string).items(), key=lambda item: item[1]))
        return res

    def create_tree(self):
        tree = []
        while len(self.sorted_string) >= 1:
            if len(tree) < 1:
                weight = self.sorted_string[0][1] + self.sorted_string[1][1]
                tree.append({
                    0: self.sorted_string.popleft(),
                    1: self.sorted_string.popleft(),
                    2: weight
                })
            else:
                if self.sorted_string:
                    for num, val in enumerate(tree):
                        weight_append = self.sorted_string[0][1]
                        weight_tree_itm = val[2]
                        weight_sum = weight_append +  weight_tree_itm
                        if weight_append < weight_tree_itm:
                            tree.insert(
                                num,
                                {
                                    0: self.sorted_string.popleft(),
                                    1: tree.pop(num),
                                    2: weight_sum
                                 })
        print(tree)
        return tree

    def create_tab(self):

        def find_tuple(dict, path=''):
            if isinstance(dict, tuple):
                self._tab[dict[0]] = path
            else:
                find_tuple(dict[0], path=f'{path}0')
                find_tuple(dict[1], path=f'{path}1')

        find_tuple(self._temp_tree)

        print(self._tab)


example = HuffmanTree()
