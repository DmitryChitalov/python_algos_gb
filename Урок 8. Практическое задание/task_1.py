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
from collections import deque, Counter


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def tree(el):
    count_el = Counter(el)
    sorted_el = deque(sorted(count_el.items(), key=lambda item: item[1]))
    while len(sorted_el) > 1:
        weight = sorted_el[0][1] + sorted_el[1][1]
        leaf = Node(left=sorted_el.popleft()[0], right=sorted_el.popleft()[0])
        for i, item in enumerate(sorted_el):
            if weight > item[1]:
                continue
            else:
                sorted_el.insert(i, (leaf, weight))
                break
        else:
            sorted_el.append((leaf, weight))
    return sorted_el[0][0]


def make_code(tree, path=''):
    if not isinstance(tree, Node):
        res_table[tree] = path
        print(path, end=' ')
    else:
        make_code(tree.left, path=f'{path}0')
        make_code(tree.right, path=f'{path}1')


res_table = dict()
string_to_code = "beep boop beer!"
get_tree = tree(string_to_code)
make_code(get_tree)
print()

for i, j in res_table.items():
    print(f'el: "{i}"  =  {j}')
'''
Добавил элементы ООП
'''
