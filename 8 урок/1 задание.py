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

class haffman:

    def __init__(self, s):
        self.code = dict()
        self.text = s

    def fanc_haffman(self):
        count = Counter(self.text)
        sort = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sort) != 1:
            while len(sort) > 1:
                equate = sort[0][1] + sort[1][1]
                comb = {0: sort.popleft()[0], 1: sort.popleft()[0]}
                for i, _count in enumerate(sort):
                    if equate > _count[1]:
                        continue
                    else:
                        sort.insert(i, (comb, equate))
                        break
                else:
                    sort.append((comb, equate))
        else:
            equate = sort[0][1]
            comb = {0: sort.popleft()[0], 1: None}
            sort.append((comb, equate))
        return sort[0][0]

    def fanc_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code[tree] = path
        else:
            self.fanc_code(tree[0], path=f'{path}0')
            self.fanc_code(tree[1], path=f'{path}1')
        return
    def print_code(self):
        self.fanc_code(self.fanc_haffman())
        for i in self.text:
            print(self.code[i], end=' ')
        print()
        return

s = "beep boop beer!"
haff = haffman(s)
haff.print_code()








