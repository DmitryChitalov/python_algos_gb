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
from timeit import timeit


def list_append(value):
    my_list = []
    for i in range(value):
        my_list.append(i)


def deque_append(value):
    my_list = deque()
    for i in range(value):
        my_list.append(i)


def list_append_left(value):
    my_list = []
    for i in range(value):
        my_list.insert(0, i)


def deque_append_left(value):
    my_list = deque()
    for i in range(value):
        my_list.appendleft(i)


def list_extend(list_range):
    my_list = []
    my_list.extend(list_range)


def deque_extend(list_range):
    my_list = deque()
    my_list.extend(list_range)


def list_extend_left(list_range):
    my_list = []
    for el in list_range:
        my_list.insert(0, el)


def list_pop(list_range):
    for i in range(len(list_range)):
        res = list_range.pop()


def deque_pop(list_range):
    for i in range(len(list_range)):
        res = list_range.pop()


def deque_pop_left(list_range):
    for i in range(len(list_range)):
        res = list_range.popleft()


def list_reverse(list_range):
    res = list_range.reverse()


def deque_reverse(list_range):
    res = list_range.reverse()


val_1 = 10101
val_2 = [el for el in range(10101)]

print('list_append = ',
      timeit("list_append(val_1)",
             setup="from __main__ import list_append, val_1",
             number=10000))

print('deque_append = ',
      timeit("deque_append(val_1)",
             setup="from __main__ import deque_append, val_1",
             number=10000))

print('list_append_left = ',
      timeit("list_append_left(val_1)",
             setup="from __main__ import list_append_left, val_1",
             number=10000))

print('deque_append_left = ',
      timeit("deque_append_left(val_1)",
             setup="from __main__ import deque_append_left, val_1",
             number=10000))

print('list_extend = ',
      timeit("list_extend(val_2)",
             setup="from __main__ import list_extend, val_2",
             number=10000))

print('list_extend_left = ',
      timeit("list_extend_left(val_2)",
             setup="from __main__ import list_extend_left, val_2",
             number=10000))

print('list_pop = ',
      timeit("list_pop(val_2)",
             setup="from __main__ import list_pop, val_2",
             number=10000))

print('deque_pop = ',
      timeit("deque_pop(val_2)",
             setup="from __main__ import deque_pop, val_2",
             number=10000))

print('deque_pop_left = ',
      timeit("deque_pop_left(val_2)",
             setup="from __main__ import deque_pop_left, val_2",
             number=10000))

print('list_reverse = ',
      timeit("list_reverse(val_2)",
             setup="from __main__ import list_reverse, val_2",
             number=10000))

print('deque_reverse = ',
      timeit("deque_reverse(val_2)",
             setup="from __main__ import deque_reverse, val_2",
             number=10000))
