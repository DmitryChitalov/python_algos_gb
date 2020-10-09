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


def haffman_tree(s):
    cnt = Counter(s)
    elements = deque(sorted(cnt.items(), key=lambda item: item[1]))
    if len(elements) != 1:
        while len(elements) > 1:
            weight = elements[0][1] + elements[1][1]
            elem = {0: elements.popleft()[0], 1: elements.popleft()[0]}
            for i, j in enumerate(elements):
                if weight > j[1]:
                    continue
                else:
                    elements.insert(i, (elem, weight))
                    break
            else:
                elements.append((elem, weight))
    else:
        weight = elements[0][1]
        elem = {0: elements.popleft()[0], 1: None}
        elements.append((elem, weight))

    return elements[0][0]


codes = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        codes[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = "beep boop beer!"

print(haffman_tree(s))
haffman_code(haffman_tree(s))
print(codes)

for i in s:
    print(codes[i], end=' ')
print()

"""
Решил не изобретать велосипед и рассмотреть пример из урока.
Не нашел вариантов как данный код ещё оптимизировать или использовать другие коллекции.
В итоге получилось копипаст с изменением имен переменных.
"""