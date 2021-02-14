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
from collections import deque


def haffman(sours_str):
    count_char = Counter(sours_str)
    sort_char = deque(sorted(count_char.items(), key=lambda item: item[1]))
    if len(sort_char) != 1:
        while len(sort_char) > 1:
            wight = sort_char[0][1] + sort_char[1][1]
            knot_comb = {0: sort_char.popleft()[0], 1: sort_char.popleft()[0]}
            for element, count_element in enumerate(sort_char):
                if wight > count_element[1]:
                    continue
                else:
                    sort_char.insert(element, (knot_comb, wight))
                    break
            else:
                sort_char.append((knot_comb, wight))
    else:
        wight = sort_char[0][0]
        knote_comb = {0: sort_char.popleft()[0], 1: None}
        sort_char.append((knote_comb, wight))
    return sort_char[0][0]


code_dict = dict()


def haffman_cod(tree, patch=''):
    if not isinstance(tree, dict):
        code_dict[tree] = patch
    else:
        haffman_cod(tree[0], patch=f"{patch}0")
        haffman_cod(tree[1], patch=f"{patch}1")


string ="beep boop beer!"
haffman_cod(haffman(string))

for index in string:
    print(code_dict[index], end = ' ')


"""
Взял готовое решение.
"""