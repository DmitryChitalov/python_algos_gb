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


def tree(data):
    freq_el = Counter(data)
    sort_freq = sorted(freq_el.items(), key=lambda pair: pair[1])
    while len(sort_freq) > 1:
        w = sort_freq[0][1] + sort_freq[1][1]
        tmp = {0: sort_freq.pop(0)[0], 1: sort_freq.pop(0)[0]}
        i = 0
        for el in sort_freq:
            if el[1] >= w:
                sort_freq.insert(i, (tmp, w))
                break
        else:
            sort_freq.append((tmp, w))
    return sort_freq[0][0]


def haffman_code(tree, code=""):
    if not isinstance(tree, dict):
        code_table[tree] = code
    else:
        haffman_code(tree[0], code=code + "0")
        haffman_code(tree[1], code=code + "1")


code_table = dict()

text = "beep boop beer!"
haffman_code(tree(text))

print(code_table)
for i in text:
    print(code_table[i], end=" ")