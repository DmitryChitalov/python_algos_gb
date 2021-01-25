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


def request_str():
    result = input('Введите строку: ')
    return result


def haffman_tree(my_str):
    my_dict = Counter(my_str)
    sort_lst = deque(sorted(my_dict.items(), key=lambda item: item[1]))
    if len(sort_lst) != 1:
        while len(sort_lst) > 1:
            value = sort_lst[0][1] + sort_lst[1][1]
            connect = {0: sort_lst.popleft()[0], 1: sort_lst.popleft()[0]}
            for i, old_value in enumerate(sort_lst):
                if value > old_value[1]:
                    continue
                else:
                    sort_lst.insert(i, (connect, value))
                    break
            else:
                sort_lst.append((connect, value))
    else:
        value = sort_lst[0][1]
        connect = {0: sort_lst.popleft()[0], 1: None}
        sort_lst.append((value, connect))
    return sort_lst[0][0]


table_code = {}


def haffman_code(my_tree, path=''):
    if not isinstance(my_tree, dict):
        table_code[my_tree] = path
    else:
        haffman_code(my_tree[0], path=f'{path}0')
        haffman_code(my_tree[1], path=f'{path}1')


def conclusion(my_str):
    for i in my_str:
        print(table_code[i], end=' ')
    print()


def start():
    text = request_str()
    print(f'Дерево:\n{haffman_tree(text)}')
    haffman_code(haffman_tree(text))
    print(f'Таблица кодов:\n{table_code}')
    print('Введенная строка кодом Хафмана:')
    conclusion(text)


start()
