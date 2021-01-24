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

def get_tree(deq : deque):
    while len(deq) != 1:
        is_insert = False
        temp_dict = dict()
        summ = 0
        temp_dict[0] = deq[0][0]
        summ = summ + deq[0][1]
        deq.popleft()
        temp_dict[1] = deq[0][0]
        summ = summ + deq[0][1]
        deq.popleft()
        t = temp_dict, summ
        if len(deq) == 0:
            deq.append(t)
        else:
            for i in range(len(deq)):
                if deq[i][1] >= summ:
                    deq.insert(i,t)
                    is_insert = True
                    break
                if (is_insert == False) and (i == len(deq) - 1):
                    deq.append(t)
                    is_insert = True
                    break
    return my_deque

def get_node_codes(tree, storage = {} , code = ''):
    if isinstance(tree, dict):
        get_node_codes(tree[0], storage, f'{code}0')
        get_node_codes(tree[1], storage, f'{code}1')
    else:
        storage[tree] = code


s = 'beep boop beer!'
counter_dict = Counter(s)
my_deque = deque(sorted(counter_dict.items(), key=lambda value: value[1]))

get_tree(my_deque)
my_tree = my_deque[0][0]
print('Построенное дерево на основе словаря:',my_tree)

store = dict()
get_node_codes(my_tree, store)
print('Результирующая таблица кодов:',store)

"""
Реализовал кодирование по алгоритму Хаффмана без ООП, на основе словаря.
Результат работы программы:

Построенное дерево на основе словаря: {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
Результирующая таблица кодов: {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

Получилось!
"""