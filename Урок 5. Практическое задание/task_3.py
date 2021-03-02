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

lst = [el for el in range(100)]

deq = deque()
deq.extend(lst)


def list_append(lst):
    for i in range(len(lst)):
        lst.append(i)


def deque_append(deq):
    lst = deque()
    for i in range(len(deq)):
        lst.append(i)


def lst_rmv(lst):
    for i in range(len(lst)):
        a = lst.pop()


def deq_rmv(lst):
    for i in range(len(lst)):
        a = lst.pop()


name_list = 'list_append deque_append lst_rmv deq_rmv'.split()

for id, func_name in enumerate(name_list):
    if func_name == 'list_append' or func_name == 'lst_rmv':
        print(
            f"{func_name}",
            timeit(stmt=func_name + f'({lst})',
                   number=1000,
                   globals=globals()))
    if func_name == 'deque_append' or func_name == 'deq_rmv':
        print(
            f"{func_name}",
            timeit(stmt=func_name + f'({deq})',
                   number=1000,
                   globals=globals()))


'''
добавление/удаление примерно одинаковое

'''
