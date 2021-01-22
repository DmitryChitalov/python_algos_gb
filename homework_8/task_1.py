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
'''Поскольку я плохо понял тему, сделал реализацию на основе примера из урока. Изменены имена переменных
и вместо deque использован обычный список'''


from collections import Counter

def haf_tree(string):

    count_freq = Counter(string)
    sorted_elems = list(sorted(count_freq.items(), key=lambda item: item[1]))

    if len(sorted_elems) != 1:

        while len(sorted_elems) > 1:

            weight = sorted_elems[0][1] + sorted_elems[1][1]

            combined = {0: sorted_elems.pop(0)[0],
                    1: sorted_elems.pop(0)[0]}

            for i, _count in enumerate(sorted_elems):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elems.insert(i, (combined, weight))
                    break
            else:

                sorted_elems.append((combined, weight))

    else:
        weight = sorted_elems[0][1]
        combined = {0: sorted_elems.pop(0)[0], 1: None}
        sorted_elems.append((combined, weight))

    return sorted_elems[0][0]

code_tab = dict()

def haf_code(node, symb=''):
    if not isinstance(node, dict):
        code_tab[node] = symb
    else:
        haf_code(node[0], symb=f'{symb}0')
        haf_code(node[1], symb=f'{symb}1')

string = "beep boop beer!"

haf_code(haf_tree(string))

for i in string:
    print(code_tab[i], end=' ')
print()