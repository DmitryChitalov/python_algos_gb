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


user_string = 'beep boop beer!'
count = Counter(user_string)
string = deque(sorted(count.items(), key=lambda symbol: symbol[1]))


def huffman_tree(s):
    if len(s) != 1:
        while len(s) > 1:
            element = s[0][1] + s[1][1]
            comb = {0: s.popleft()[0],
                    1: s.popleft()[0]}
            for i, y in enumerate(s):
                if element > y[1]:
                    continue
                else:
                    s.insert(i, (comb, element))
                    break
            else:
                s.append((comb, element))

    else:
        element = s[0][1]
        comb = {0: s.popleft()[0], 1: None}
        s.append((comb, element))
    return s[0][0]


some_dict = {}


def huffman_code(tree, path=''):
    if not isinstance(tree, dict):
        some_dict[tree] = path
    else:
        huffman_code(tree[0], path=f'{path}0')
        huffman_code(tree[1], path=f'{path}1')


huffman_code(huffman_tree(string))


for i in user_string:
    print(some_dict[i], end=' ')


