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
from collections import Counter

def assign_code(nodes, label, result, prefix=''):
    childs = nodes[label]
    tree = {}
    if len(childs) == 2:
        tree['0'] = assign_code(nodes, childs[0], result, prefix + '0')
        tree['1'] = assign_code(nodes, childs[1], result, prefix + '1')
        return tree
    else:
        result[label] = prefix
        return label

def Huffman_code(_vals):
    vals = _vals.copy()#создаем копию осортированного списка
    nodes = {}
    for n in vals.keys():  # инициализация листьев
        nodes[n] = []

    while len(vals) > 1:  #создание бинарного дерева
        s_vals = sorted(vals.items(), key=lambda x: x[1])
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        vals[a1 + a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1 + a2] = [a1, a2]
    code = {}
    root = a1 + a2
    tree = assign_code(nodes, root, code)  #назначение кода для данного двоичного дерева
    return code, tree

s = input('Введите строку для кодирования: ')
freq = Counter(s).items()

vals = {l: v for (l, v) in freq}
code, tree = Huffman_code(vals)

encoded = ' '.join([code[t] for t in s])
print('Encoded text:', encoded)