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
from timeit import timeit


def haff_tree(phrase):
    sym_counter = Counter(phrase)
    sorted_counter = deque(sorted(sym_counter.items(), key=lambda item: item[1]))
    if len(sorted_counter) != 1:
        while len(sorted_counter) > 1:
            priority = sorted_counter[0][1] + sorted_counter[1][1]
            new_node = {0: sorted_counter.popleft()[0],
                        1: sorted_counter.popleft()[0]
                        }
            for posotion, elem in enumerate(sorted_counter):
                if priority > elem[1]:
                    continue
                else:
                    sorted_counter.insert(posotion, (new_node, priority))
                    break
            else:
                sorted_counter.append((new_node, priority))
    else:
        priority = sorted_counter[0][1]
        new_node = {0: sorted_counter.popleft()[0], 1: None}
        sorted_counter.append((new_node, priority))
    return sorted_counter[0][0]


codes = {}


def haff_code(h_tree, path_bit=''):
    if not isinstance(h_tree, dict):
        codes[h_tree] = path_bit
    else:
        haff_code(h_tree[0], path_bit=f'{path_bit}0')
        haff_code(h_tree[1], path_bit=f'{path_bit}1')


phrase = input('Введите строку из трех слов: ')
haff_code(haff_tree(phrase))
for sym in phrase:
    print(codes[sym], end=' ')
