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
"""Хаффман через коллекции"""

from collections import Counter, deque


class Node:
    __slots__ = ["left", "right", "char", "weight"]

    def __str__(self):
        return f'{self.left}, {self.right}, {self.char}, {self.weight}'


def haffman_tree(i_s):
    la_cnt   = Counter(i_s)
    la_chars = deque(sorted(la_cnt.items(), key=lambda item: item[1]))
    #print(' la_chars',  la_chars)
    la_elems = deque()

    for rec in la_chars:
        l_obj = Node()
        l_obj.left   = None
        l_obj.right  = None
        l_obj.char   = rec[0]
        l_obj.weight = rec[1]
        la_elems.append(l_obj)

    #for rec in la_elems:
    #    print(rec)

    if len(la_elems) != 1:
        while len(la_elems) > 1:
            l_obj = Node()
            l_obj.left  = la_elems[0]
            l_obj.right = la_elems[1]
            l_obj.char  = None
            l_obj.weight = la_elems[0].weight + la_elems[1].weight

            la_elems.popleft()
            la_elems.popleft()

            for i, rec in enumerate(la_elems):
                if l_obj.weight > rec.weight:
                    continue
                else:
                    la_elems.insert(i, l_obj)
                    break
            else:
                la_elems.append(l_obj)
    else:
        l_obj = Node()
        l_obj.left   = la_elems[0]
        l_obj.right  = None
        l_obj.char   = None
        l_obj.weight = la_elems[0].weight

        la_elems.popleft()
        la_elems.append(l_obj)

    return la_elems[0]


code_table = dict()


def haffman_code(tree, i_path=''):
    if tree.left is None and tree.right is None:
        code_table[tree.char] = i_path
    else:
        haffman_code(tree.left,  i_path=f'{i_path}0')
        haffman_code(tree.right, i_path=f'{i_path}1')

g_s = "beep boop beer!"
haffman_code(haffman_tree(g_s))

for i in g_s:
    print(code_table[i], end=' ')
print()
