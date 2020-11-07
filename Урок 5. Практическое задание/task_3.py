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
# appenfleft extendleft значительно быстрее выполняются через deque

from collections import deque
import timeit

list_with_range = [el for el in range(1000)]
deque_with_range = deque()
deque_with_range.extend(list_with_range)


def list_appendleft(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def deque_appendleft(num):
    my_list = deque()
    for i in range(num):
        my_list.appendleft(i)


name_list = ['list_appendleft', 'deque_appendleft']
num_time = 100

for id, func_name in enumerate(name_list):
    print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(100)', setup=f'from __main__ import {func_name}')}")
