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
from collections import deque, defaultdict


class HuffmanCode:
    def __init__(self, some_str):
        self.some_str = some_str
        self.count = defaultdict(int)
        self.counter_sort()
        self.tree_str = self.tree()[0][0]
        self.code_tree = dict()
        self.code(self.tree_str)

    def __str__(self):
        rez = [self.code_tree[i] for i in self.some_str]
        return f'STR = {self.some_str}\n' \
               f'TREE = {str(self.tree_str)}\n' \
               f'HUFFMAN CODING = {" ".join(rez)}'

    def counter_sort(self):
        """
        Метод считает кол-во символов в строке, и возвращает отсортированную очередь из уникальных символов
        """
        some_lst = list(self.some_str)
        for el in some_lst:
            self.count[el] += 1
        self.tree_str = deque(sorted(self.count.items(), key=lambda item: item[1]))
        return self.tree_str

    def tree(self):
        """
        Строим наше дерево
        """
        if len(self.tree_str) != 1:
            while len(self.tree_str) > 1:
                weight = self.tree_str[0][1] + self.tree_str[1][1]
                comb = {0: self.tree_str.popleft()[0],
                        1: self.tree_str.popleft()[0]}
                for i, _count in enumerate(self.tree_str):
                    if weight > _count[1]:
                        continue
                    else:
                        self.tree_str.insert(i, (comb, weight))
                        break
                else:
                    self.tree_str.append((comb, weight))
        else:
            weight = self.tree_str[0][1]
            comb = {0: self.tree_str.popleft()[0], 1: None}
            self.tree_str.append((comb, weight))
        return self.tree_str

    def code(self, tree=None, path=''):
        """
        Кодируем нашу строку
        """
        if tree is None:
            tree = self.tree_str
            self.code(tree)
        else:
            if not isinstance(tree, dict):
                self.code_tree[tree] = path
            else:
                self.code(tree[0], path=f'{path}0')
                self.code(tree[1], path=f'{path}1')


obj = HuffmanCode('beep boop beer!')
print(obj)
