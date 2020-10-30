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


def haffman_tree(leaf):
    leaf_counter = Counter(leaf)
    sorted_leaf = deque(sorted(leaf_counter.items(), key=lambda item: item[1]))

    if len(sorted_leaf) != 1:
        while len(sorted_leaf) > 1:
            weight_1 = sorted_leaf[0][1] + sorted_leaf[1][1]

            node_combination_1 = {0: sorted_leaf.popleft()[0],
                                  1: sorted_leaf.popleft()[0]}

            for i, _count in enumerate(sorted_leaf):
                if weight_1 > _count[1]:
                    continue
                else:
                    sorted_leaf.insert(i, (node_combination_1, weight_1))
                    break
            else:
                sorted_leaf.append((node_combination_1, weight_1))
    else:
        weight_2 = sorted_leaf[0][1]
        node_combination_2 = {0: sorted_leaf.popleft()[0], 1: None}
        sorted_leaf.append((node_combination_2, weight_2))

    return sorted_leaf[0][0]


code_table = dict()


def haffman_encoding(tree, path=''):

    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_encoding(tree[0], path=f'{path}0')
        haffman_encoding(tree[1], path=f'{path}1')


encoding_string = input('Enter some text to do convert by haffman code: ')

haffman_encoding(haffman_tree(encoding_string))

for i in encoding_string:
    print(code_table[i], end=' ')
