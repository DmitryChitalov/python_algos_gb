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

table = dict()


def haffman(string):
    c = Counter(string)
    elems = deque(sorted(c.items(), key=lambda item: item[1]))
    while len(elems) > 1:
        new_count = elems[0][1] + elems[1][1]
        new_element = {
            0: elems.popleft()[0],
            1: elems.popleft()[0]
        }
        i = 0
        try:
            while new_count > elems[i][1]:
                i += 1
        except IndexError:
            elems.append((new_element, new_count))
        else:
            elems.insert(i, (new_element, new_count))
    create_haffman_table(elems[0][0])
    result = ''
    for i in string:
        result += f'{table[i]} '
    return result


def create_haffman_table(t, path=''):
    if not isinstance(t, dict):
        table[t] = path
    else:
        create_haffman_table(t[0], path=f'{path}0')
        create_haffman_table(t[1], path=f'{path}1')


print(haffman("beep boop beer!"))
"""
Код писал сам основываясь на пример
"""
