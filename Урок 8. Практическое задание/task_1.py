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

"""Код взял из примера. Писал постепенно по строчке, чтобы разобраться в алгоритме. Разобрался, но 
сам бы написать не смог"""

from collections import Counter, deque


def haffman_tree(my_str):
    symbols_count = Counter(my_str)
    my_deque = deque(sorted(symbols_count.items(), key=lambda item: item[1]))
    if len(my_deque) != 1:
        while len(my_deque) > 1:
            quantity = my_deque[0][1] + my_deque[1][1]
            my_dict = {0: my_deque.popleft()[0], 1: my_deque.popleft()[0]}
            for i, elem in enumerate(my_deque):
                if quantity > elem[1]:
                    continue
                else:
                    my_deque.insert(i, (my_dict, quantity))
                    break
            else:
                my_deque.append((my_dict, quantity))
    else:
        quantity = my_deque[0][1]
        my_dict = {0: my_deque.popleft()[0], 1: None}
        my_deque.append((my_dict, quantity))
    return my_deque[0][0]


haf_table = {}


def haffman_code(haf_tree, path=''):
    if not isinstance(haf_tree, dict):
        haf_table[haf_tree] = path
    else:
        haffman_code(haf_tree[0], path=f'{path}0')
        haffman_code(haf_tree[1], path=f'{path}1')


s = "beep boop beer!"

haffman_code(haffman_tree(s))
print(haf_table)

for i in s:
    print(haf_table[i], end=' ')
