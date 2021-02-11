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
code_table = dict()


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(s):
    count = Counter(s)
    sorted_el = deque(sorted(count.items(), key=lambda item: item[1]))
    while len(sorted_el) > 1:
        weight = sorted_el[0][1] + sorted_el[1][1]
        node = MyNode(left=sorted_el.popleft()[0], right=sorted_el.popleft()[0])
        for i, _count in enumerate(sorted_el):
            if weight > _count[1]:
                continue
            else:
                sorted_el.insert(i, (node, weight))
                break
        else:
            sorted_el.append((node, weight))
    return sorted_el[0][0]


def haffman_code(tree, path=''):

    if not isinstance(tree, MyNode):
        code_table[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


input_string = "abrakadabra"
haffman_code(haffman_tree(input_string))
for i in input_string:
    print(code_table[i], end=' ')

    
"""
Тема пошла тяжело, подсмотрел в решении, немного потыкал под себя и попытался разобраться.
"""
