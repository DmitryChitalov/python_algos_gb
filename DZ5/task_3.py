"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
import timeit

list_range = [el for el in range(1000)]
deque_with_range = deque()
deque_with_range.extend(list_range)


def list_append(num):
    my_list = []
    for i in range(num):
        my_list.append(i)


def deque_append(num):
    my_list = deque()
    for i in range(num):
        my_list.append(i)


def list_appendleft(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def deque_appendleft(num):
    my_list = deque()
    for i in range(num):
        my_list.appendleft(i)


def list_extend(lst_range):
    my_list = []
    my_list.extend(lst_range)


def deque_extend(lst_range):
    my_list = deque()
    my_list.extend(lst_range)


def list_extendleft(lst_range):
    my_list = []
    for el in lst_range:
        my_list.insert(0, el)


def deque_extendleft(lst_range):
    my_list = deque()
    my_list.extendleft(lst_range)


def list_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def deque_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def list_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop(0)


def deque_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.popleft()


def list_reverse(lst_range):
    a = lst_range.reverse()


def deque_reverse(lst_range):
    a = lst_range.reverse()


name_list = 'list_append deque_append list_appendleft deque_appendleft list_extend deque_extend list_extendleft deque_extendleft list_pop deque_pop list_popleft deque_popleft list_reverse deque_reverse'.split()

num_time = 10000

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print("*" * 30)
    if id <= 3:
        print(
            f"{func_name} -   {timeit.timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    else:
        if id % 2 == 0:
            print(
                f"{func_name}(list_with_range) -  {timeit.timeit(stmt=func_name + f'({list_range})', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
        else:
            print(
                f"{func_name}(deque_with_range) - {timeit.timeit(stmt=func_name + f'({deque_with_range})', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")

'''
deque значительно лучше выполняет свои функции: append слева и extend слева и pop слева
Если говорить о appendleft и extendleft
Единственный эффективный аналог insert в обычном листе намного хуже выполняет то же самое действие
Если говорить о Popleft, то аналог присвоить значениее и remove работает в два раза хуже
Единственный минус deque - плохо работает deque с функцией reverse (в два раза медленней)
По пунктам же обычного списка (добавление, pop, extend) время примерно одинаковое
******************************
list_append -   1.3150439999999999
deque_append -   1.3521586999999997
******************************
list_appendleft -   7.844732199999999
deque_appendleft -   1.2810194
******************************
list_extend(list_with_range) -  0.14090520000000062
deque_extend(deque_with_range) - 0.4056160999999996
******************************
list_extendleft(list_with_range) -  7.756557900000001
deque_extendleft(deque_with_range) - 0.3858503000000013
******************************
list_pop(list_with_range) -  1.3232186000000006
deque_pop(deque_with_range) - 1.547935299999999
******************************
list_popleft(list_with_range) -  4.391415199999997
deque_popleft(deque_with_range) - 1.2548226000000007
******************************
list_reverse(list_with_range) -  0.08545730000000162
deque_reverse(deque_with_range) - 0.23782139999999785
'''
