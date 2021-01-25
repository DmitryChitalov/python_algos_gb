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


def func_haffman_tree(str):

    count_elements = Counter(str)

    sorted_count_elements = deque(sorted(count_elements.items(), key=lambda item: item[1]))
    print( sorted_count_elements)

    if len(sorted_count_elements) != 1:

        while len(sorted_count_elements) > 1:

            weight = sorted_count_elements[0][1] + sorted_count_elements[1][1]

            combination = {0: sorted_count_elements.popleft()[0],
                    1: sorted_count_elements.popleft()[0]}


            for i, _count in enumerate(sorted_count_elements):

                if weight > _count[1]:
                    continue
                else:

                    sorted_count_elements.insert(i, (combination, weight))
                    break
            else:


                sorted_count_elements.append((combination, weight))

    else:

        weight = sorted_count_elements[0][1]
        combination = {0: sorted_count_elements.popleft()[0], 1: None}
        sorted_count_elements.append((combination, weight))

    return sorted_count_elements[0][0]


haff_code_table = dict()

def func_haffman_code(tree, path=''):

    if not isinstance(tree, dict):
        haff_code_table[tree] = path

    else:
        func_haffman_code(tree[0], path=f'{path}0')
        func_haffman_code(tree[1], path=f'{path}1')


str = "beep boop beer!"


func_haffman_code(func_haffman_tree(str))


for i in str:
    print(haff_code_table[i], end=' ')
print()