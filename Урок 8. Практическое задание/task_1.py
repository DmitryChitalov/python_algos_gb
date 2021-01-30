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
    tree = {}
    code_table = {}

    def __init__(self, string):
        self.string = string

    def create_tree(self):
        temp = Counter(self.string)
        source_list = list(sorted(temp.items(), key=lambda item: item[1]))
        if len(source_list) > 1:
            while len(source_list) > 1:
                number = source_list[0][1] + source_list[1][1]
                summ = {0: source_list.pop(0)[0],
                        1: source_list.pop(0)[0]}
                check = 0
                for x in range(len(source_list)):
                    if number <= source_list[x][1]:
                        source_list.insert(x, (summ, number))
                        check += 1
                        break
                if check == 0:
                    source_list.append((summ, number))
        else:
            number = source_list[0][1]
            summ = {0: source_list.pop(0)[0], 1: 'Exit'}
            source_list.append((summ, number))
        Tree.tree = source_list[0][0]

    def create_code_table(self, tree=None, path=''):
        if tree is None:
            tree = Tree.tree

        if not tree:
            print('Please call method create_tree')
        else:
            if not isinstance(tree, dict):
                Tree.code_table[tree] = path
            else:
                self.create_code_table(tree[0], path=f'{path}0')
                self.create_code_table(tree[1], path=f'{path}1')

    def get_code(self):
        if not Tree.tree:
            print('please call method create_tree')
        elif not Tree.code_table:
            print('please call method create_code_table')
        else:
            for x in self.string:
                print(f'{Tree.code_table[x]}', end=' ')


s = 'beep boop beer!'
obj_test = Tree(s)
obj_test.create_tree()
obj_test.create_code_table()
# print(obj_test.tree)
# print(obj_test.code_table)
obj_test.get_code()
