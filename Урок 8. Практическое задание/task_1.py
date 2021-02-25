"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque


def haffman_tree(s):
    count = Counter(s)
    # Counter({'a': 1, 'b': 1, 'o': 1, 'r': 3, 't': 2, 'e': 1, 'y': 1, ' ': 1})
    sorted_elems = deque(sorted(count.items(), key=lambda item: item[1]))
    # deque([('a', 1), ('b', 1), ('o', 1), ('e', 1), ('y', 1), (' ', 1), ('t', 2), ('r', 3)])
    if len(sorted_elems) != 1:
       while len(sorted_elems) > 1:
           #веса - 2, 2, 2, 4, 7, 11
            weight = sorted_elems[0][1] + sorted_elems[1][1]
            comb = {0: sorted_elems.popleft()[0],
                    1: sorted_elems.popleft()[0]}
            for i, _count in enumerate(sorted_elems):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elems.insert(i, (comb, weight))
                    break
            else:
                sorted_elems.append((comb, weight))
    else:
        weight = sorted_elems[0][1]
        comb = {0: sorted_elems.popleft()[0], 1: None}
        sorted_elems.append((comb, weight))
    return sorted_elems[0][0]


code_line = dict()

def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_line[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = "abort retry"

haffman_code(haffman_tree(s))

for i in s:
    print(code_line[i], end=' ')
print()
