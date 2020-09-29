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

import timeit
import random
from collections import deque

n = 1000


def set_lst(n):
    lst = [random.randint(0, n) for i in range(n)]
    return lst


def set_deque(n):
    deq_obj = deque(set_lst(n))
    return deq_obj


def insert_left_lst(lst, itm):
    lst.insert(0, itm)
    return lst


def insert_left_deque(deq, itm):
    deq.appendleft(itm)
    return deq


def remove_left_lst(lst, itm):
    lst.remove(itm)


def remove_left_deque(deq, itm):
    deq.remove(itm)


def index_left_lst(lst, itm):
    lst.index(itm)


def index_left_deque(deq, itm):
    deq.index(itm)


lst = set_lst(n)

deq = set_deque(n)

itm = 111

print(timeit.timeit('set_lst(n)', setup="from __main__ import set_lst, n", number=1000))
print(timeit.timeit('set_deque(n)', setup="from __main__ import set_deque, n", number=1000))
print(timeit.timeit('insert_left_lst(lst, itm)', setup="from __main__ import insert_left_lst, lst, itm", number=1000))
print(
    timeit.timeit('insert_left_deque(deq, itm)', setup="from __main__ import insert_left_deque, deq, itm", number=1000))
lst = insert_left_lst(lst, itm)
deq = insert_left_deque(deq, itm)
print(timeit.timeit('index_left_lst(lst, itm)', setup="from __main__ import index_left_lst, lst, itm", number=1000))
print(timeit.timeit('index_left_deque(deq, itm)', setup="from __main__ import index_left_deque, deq, itm", number=1000))
print(timeit.timeit('remove_left_lst(lst, itm)', setup="from __main__ import remove_left_lst, lst, itm", number=1000))
print(
    timeit.timeit('remove_left_deque(deq, itm)', setup="from __main__ import remove_left_deque, deq, itm", number=1000))
"""Утверждение в условии верно"""