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


class HaffmanTree:
    def __init__(self, string):
        self.string = string
        self.tree = None
        self.count = None
        self.root = None
        self.comb = None

    def counter_str(self):
        self.count = Counter(self.string)

    def deq_sort(self):
        self.tree = deque(sorted(self.count.items(), key=lambda el: el[1]))

    def step(self):
        self.comb = {'0': self.tree.popleft()[0], '1': self.tree.popleft()[0]}

    def construction_tree(self):
        HaffmanTree.counter_str(self)
        HaffmanTree.deq_sort(self)
        while len(self.tree) > 1:
            root = self.tree[0][1] + self.tree[1][1]
            HaffmanTree.step(self)
            for i, el in enumerate(self.tree):
                if el[1] < root:
                    continue
                else:
                    self.tree.insert(i, (self.comb, root))
                    break
            else:
                self.tree.append((self.comb, root))

    def get_tree(self):
        return self.tree[0][0]


class HaffmanCode:
    def __init__(self, tree):
        self.tree = tree
        self.dict_code = {}

    def collect_code(self, tree,  path=''):
        if isinstance(tree, str):
            self.dict_code[tree] = path
        else:
            self.collect_code(tree['0'], path=f'{path}0')
            self.collect_code(tree['1'], path=f'{path}1')

    def get_dict_code(self):
        HaffmanCode.collect_code(self, self.tree)
        return self.dict_code


def haffman_code(words):
    tree = HaffmanTree(words)
    tree.construction_tree()
    code = HaffmanCode(tree.get_tree())
    dict_code = code.get_dict_code()
    code_str = ''
    for i in words:
        code_str += (dict_code[i] + ' ')
    return code_str


if __name__ == '__main__':
    word = "beep boop beer!"
    print(haffman_code(word))


