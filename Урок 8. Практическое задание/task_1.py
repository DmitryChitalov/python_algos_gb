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

srt_ = 'beep boop beer!'
count_ = Counter(srt_)
sorted_count_ = deque(sorted(count_.items(), key = lambda item: item[1]))

def haffman_tree(deq):
    for i in range(len(deq)):
        if len(deq) > 2:
            weight = deq[0][1] + deq[1][1]
            d_tree = {0: deq.popleft()[0] ,
                      1: deq.popleft()[0]}
            for n, ii in enumerate(deq):
                if weight > ii[1]:
                    if n+1 == len(deq):
                        deq.insert(n+1, (d_tree, weight))
                        break
                    continue
                else:
                    deq.insert(n, (d_tree, weight))
                    break
        else:
            return {0: {0: deq.popleft()[0] , 1: deq.popleft()[0]}}


ddd = haffman_tree(sorted_count_)
print(ddd)

code_table = dict()

def haffman_code(tree, path=''):
    if isinstance(tree, dict):
        haffman_code(tree[0],f'{path}0')
        haffman_code(tree[1],f'{path}1')
    else:
        code_table[tree] = path
    return code_table

# последний ноль в словарь добавлять не нужно было, как я понял...
print(haffman_code(ddd[0]))