"""
Задача 3.
В соответствии с документацией Python, deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить,
используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from collections import deque # импорт из collections
from timeit import timeit # для замеров

list_with_range = [el for el in range(1000)] # список
deque_with_range = deque() # дек
deque_with_range.extend(list_with_range) # дек со списком


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


name_list = 'list_append deque_append list_appendleft deque_appendleft' \
            ' list_extend deque_extend list_extendleft deque_extendleft ' \
            'list_pop deque_pop list_popleft deque_popleft ' \
            'list_reverse deque_reverse'.split()

# Для чистоты эксперимента, если в функцию подается список,
# то для deque будет подаваться deque список, для list соотвественно list

num_time = 10000

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print()
    if id <= 3:
        print(
            f"{func_name} -",
            timeit(stmt=func_name + f'(1000)',
                   number=num_time,
                   globals=globals()))
    else:
        if id % 2 == 0:
            print(
                f"{func_name}(list_with_range.copy()) -",
                timeit(stmt=func_name + f'({list_with_range})',
                       number=num_time,
                       globals=globals()))
        else:
            print(
                f"{func_name}(deque_with_range.copy()) -",
                timeit(stmt=func_name + f'({deque_with_range})',
                       number=num_time,
                       globals=globals()))

'''
deque значительно лучше выполняет свои функции: append слева и extend 
слева и pop слева
Если говорить о appendleft и extendleft
Единственный эффективный аналог insert в обычном листе намного хуже 
выполняет то же самое действие
Если говорить о Popleft, то аналог присвоить значениее и remove 
работает в два раза хуже
Единственный минус deque - плохо работает deque с функцией reverse 
(в два раза медленней)
По пунктам же обычного списка (добавление, pop, extend) 
время примерно одинаковое

list_append - 0.618401924
deque_append - 0.6080148900000001

list_appendleft - 3.9198680020000003
deque_appendleft - 0.5858106049999998 !

list_extend(list_with_range.copy()) - 0.0764106559999993
deque_extend(deque_with_range.copy()) - 0.1703434330000002

list_extendleft(list_with_range.copy()) - 3.898445839
deque_extendleft(deque_with_range.copy()) - 0.1675835190000008 !

list_pop(list_with_range.copy()) - 0.8521026430000003
deque_pop(deque_with_range.copy()) - 0.6595787710000014

list_popleft(list_with_range.copy()) - 2.349823894
deque_popleft(deque_with_range.copy()) - 0.6567548619999997 !

list_reverse(list_with_range.copy()) - 0.054979437000000075
deque_reverse(deque_with_range.copy()) - 0.1091667910000016
'''
