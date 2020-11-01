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


def haffman_tree(s):
    count = Counter(s)
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sorted_elements) > 1:
        while len(sorted_elements) > 1:
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            for i, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elements.insert(i, (comb, weight))
                    break
            else:
                sorted_elements.append((comb, weight))
    #я не стал менять названия переменным, но сделал доработку на тот случай если список окажется пустым или None
    elif len(sorted_elements) == 1:
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    else:
        comb = {0: None, 1: None}
        sorted_elements.append((comb, 0))
    return sorted_elements[0][0]


code_table = dict()

def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = '123543234'

haffman_code(haffman_tree(s))

print(code_table)

for i in s or '':
    print(code_table[i], end=' ')
print()
'''
s=None
ничего не выводится
s=''
ничего не выводится
s = '123543234'
000 01 11 001 10 11 01 11 10 
'''