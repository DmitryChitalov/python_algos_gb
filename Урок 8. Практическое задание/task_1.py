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


test_str = input('Введите строку, которую Хаффман будет кодировать :')
c = Counter(test_str)
tree = deque(sorted(c.items(), key=lambda el: el[1]))
while len(tree) > 1:
    w_sum = tree[0][1] + tree[1][1]
    sub_tree = {0: tree.popleft()[0], 1: tree.popleft()[0]}
    max_i = len(tree) - 1
    for i, el in enumerate(tree):
        if w_sum <= el[1]:
            tree.insert(i, (sub_tree, w_sum))
            break
        elif i == max_i:
            tree.append((sub_tree, w_sum))
            break
    if not len(tree):
        tree.insert(0, (sub_tree, w_sum))
huff_dict = {}


def huff_dict_recurse(obj, code=''):
    if type(obj) is str:
        huff_dict[obj] = code
    else:
        huff_dict_recurse(obj[0], f'{code}0')
        huff_dict_recurse(obj[1], f'{code}1')


huff_dict_recurse(tree[0][0])
print(test_str)
print(tree[0][0])
print(huff_dict)
[print(huff_dict[s], end=' ') for s in test_str]


'''
Введите строку, которую Хаффман будет кодировать :Мама мыла раму.
Мама мыла раму.
{0: {0: 'м', 1: {0: {0: 'М', 1: 'ы'}, 1: ' '}}, 1: {0: {0: {0: 'у', 1: '.'}, 1: {0: 'л', 1: 'р'}}, 1: 'а'}}
{'м': '00', 'М': '0100', 'ы': '0101', ' ': '011', 'у': '1000', '.': '1001', 'л': '1010', 'р': '1011', 'а': '11'}
0100 11 00 11 011 00 0101 1010 11 011 1011 11 00 1000 1001 
'''