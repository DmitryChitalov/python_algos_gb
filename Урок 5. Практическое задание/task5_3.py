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

list_with_range = [el for el in range(1000)]
deque_with_range = deque()
deque_with_range.extend(list_with_range)


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
    if id%2==0:
        print()
    if id<=3:
        print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    else:
        if id%2==0:
            print(f"{func_name}(list_with_range) -\t{timeit.timeit(stmt=func_name + f'({list_with_range})', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
        else:
            print(f"{func_name}(deque_with_range) -\t{timeit.timeit(stmt=func_name + f'({deque_with_range})', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")


'''
list_append -	1.8343172
deque_append -	1.5493959
deque здесь предпочтительнее, но не намного

list_appendleft -	5.038468399999999
deque_appendleft -	1.6020734999999995
deque в данном случае работает в 3 раза быстее

list_extend(list_with_range) -	0.13211929999999938
deque_extend(deque_with_range) -	0.33709349999999993
list здесь предпочтительне

list_extendleft(list_with_range) -	4.5863192999999995
deque_extendleft(deque_with_range) -	0.30548530000000085
deque здесь отработало в 15 раз быстее

list_pop(list_with_range) -	1.4849945999999985
deque_pop(deque_with_range) -	1.6098946000000005
list здесь предпочтительне

list_popleft(list_with_range) -	2.9865627000000003
deque_popleft(deque_with_range) -	1.4565590999999998
deque здесь предпочтительнее

list_reverse(list_with_range) -	0.09283000000000285
deque_reverse(deque_with_range) -	0.23248549999999923
list здесь отработало в 2,5 раз быстее


'''