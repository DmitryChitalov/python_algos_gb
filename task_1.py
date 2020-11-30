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
from pprint import pprint

s = "beep boop beer!"


def decorator(func):
    def coding_haf(el):
        el = Counter(el)
        el = sorted(el.items(), key=lambda i: i[1])
        while len(el) > 1:
            weight = el[0][1] + el[1][1]
            temp = {0: el.pop(0)[0], 1: el.pop(0)[0]}

            for i, j in enumerate(el):
                if j[1] >= weight:
                    el.insert(i, (temp, weight))
                    break
            else:
                el.append((temp, weight))
        else:
            el = el.pop(0)[0]
        print(el)
        return func(el)

    return coding_haf


@decorator
def encoding_haf_wrap(el_wrap, sequence_wrap=''):
    haf_dict = {}

    def encoding_haf(el, sequence):
        if not isinstance(el, dict):
            haf_dict[el] = sequence
        else:
            encoding_haf(el[0], sequence + "0")
            encoding_haf(el[1], sequence + "1")

    encoding_haf(el_wrap, sequence_wrap)
    for i, j in haf_dict.items():
        print(j, end=' ')


encoding_haf_wrap(s)
