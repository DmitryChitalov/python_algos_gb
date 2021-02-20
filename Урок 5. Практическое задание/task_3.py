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

from timeit import timeit
from collections import deque

n = 999
lists = [i for i in range(n)]
deq = deque(lists)


def append_first(n):
    lists = []
    for i in range(n):
        lists.insert(0, i)


def append_last(n):
    lists = []
    for i in range(n):
        lists.append(i)


def pop_first(lists):
    for i in range(len(lists)):
        lists.pop(0)


def pop_last(lists):
    for i in range(len(lists)):
        lists.pop()


def pop_last_deq(deq):
    for i in range(len(deq)):
        deq.pop()


def pop_first_deq(deq):
    for i in range(len(deq)):
        deq.popleft()


def append_last_deq(n):
    deq = deque()
    for i in range(n):
        deq.append(i)


def append_first_deque(n):
    deq = deque()
    for i in range(n):
        deq.appendleft(i)


def print_timeint(func_name, n):
    print(f'{func_name} {timeit(f"{func_name}({n})", globals=globals(), number=10000)}')


print_timeint('append_first', n)
print_timeint('append_first_deque', n)
print_timeint('append_last', n)
print_timeint('append_last_deq', n)
print_timeint('pop_first', lists)
print_timeint('pop_first_deq', deq)
print_timeint('pop_last', lists)
print_timeint('pop_last_deq', deq)


print('deq существенно быстрее при добавлении данных в массив')
