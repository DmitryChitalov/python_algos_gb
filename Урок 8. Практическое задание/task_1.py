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

from collections import Counter, deque


class Haffman:
    def __init__(self, string):
        # изначальная строка
        self.noncoding = string

    def haffman_tree(self):
        count = Counter(self.noncoding)
        sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sorted_elements) != 1:
            while len(sorted_elements) > 1:
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                comb = {0: sorted_elements.popleft()[0],
                        1: sorted_elements.popleft()[0]}
                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    sorted_elements.append((comb, weight))
        else:
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))
        self.haffman_tree = sorted_elements[0][0]
        return self.haffman_tree

    def haffman_table(self, tree = {}, path= '', code_table = dict()):
        if path == '':
            tree = dict(self.haffman_tree)
        if not isinstance(tree, dict):
            code_table[tree] = path
        else:
            self.haffman_table(tree[0], path=f'{path}0')
            self.haffman_table(tree[1], path=f'{path}1')
        return code_table

    def haffman_codding(self):
        s = self.noncoding
        table = self.haffman_table()
        code_string = ''
        for i in s:
           code_string += f'{table[i]} '
        return code_string


s = Haffman("beep boop beer!")
print(s.haffman_tree())
print(s.haffman_table())
print(s.haffman_codding())
s = Haffman("aaabbc")
print(s.haffman_tree())
print(s.haffman_table())
print(s.haffman_codding())