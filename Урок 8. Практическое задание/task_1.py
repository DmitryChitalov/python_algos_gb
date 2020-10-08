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


def create_tree(input_str):
    unique_elems = Counter(input_str)
    sorted_elems = deque(sorted(unique_elems.items(), key=lambda el: el[1]))
    if len(sorted_elems) != 1:
        while len(sorted_elems) > 1:
            weight = sorted_elems[0][1] + sorted_elems[1][1]
            result_tree = {0: sorted_elems.popleft()[0],
                           1: sorted_elems.popleft()[0]}

            for i, unique_elems in enumerate(sorted_elems):
                if weight > unique_elems[1]:
                    continue
                else:
                    sorted_elems.insert(i, (result_tree, weight))
                    break
            else:
                sorted_elems.append((result_tree, weight))
    else:
        weight = sorted_elems[0][1]
        result_tree = {0: sorted_elems.popleft()[0], 1: None}
        sorted_elems.append((result_tree, weight))
    return sorted_elems[0][0]


code_table = dict()


def make_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        make_code(tree[0], path=f'{path}0')
        make_code(tree[1], path=f'{path}1')


my_string = "hello world!"

make_code(create_tree(my_string))

for i in my_string:
    print(code_table[i], end=' ')
print()
