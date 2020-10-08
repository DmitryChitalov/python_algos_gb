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


def func_tree(str):
    count = Counter(str)
    sort_el = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sort_el) != 1:
        while len(sort_el) > 1:
            a = sort_el[0][1] + sort_el[1][1]
            b = {0: sort_el.popleft()[0], 1: sort_el.popleft()[0]}
            for i, _count in enumerate(sort_el):
                if a > _count[1]:
                    continue
                else:
                    sort_el.insert(i, (b, a))
                    break
            else:
                sort_el.append((b, a))
    else:
        a = sort_el[0][1]
        b = {0: sort_el.popleft()[0], 1: None}
        sort_el.append((b, a))
    return sort_el[0][0]


dic = dict()

def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        dic[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


str = input('Input word: ')

haffman_code(func_tree(str))

for i in str:
    print(dic[i], end=' ')