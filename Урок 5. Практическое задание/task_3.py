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

n = 1000
my_list = [i for i in range(n)]
my_deq = deque(my_list)


def append_left_list(n):
    my_list = []
    for i in range(n):
        my_list.insert(0, i)


def append_right_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)


def pop_left_list(my_list):
    for i in range(len(my_list)):
        my_list.pop(0)


def pop_right_list(my_list):
    for i in range(len(my_list)):
        my_list.pop()


def pop_right_deque(my_deque):
    for i in range(len(my_deque)):
        my_deque.pop()


def pop_left_deque(my_deque):
    for i in range(len(my_deque)):
        my_deque.popleft()


def append_right_deque(n):
    my_deque = deque()
    for i in range(n):
        my_deque.append(i)


def append_left_deque(n):
    my_deque = deque()
    for i in range(n):
        my_deque.appendleft(i)


def print_timeint(func_name, n):
    print(f'{func_name} {timeit(f"{func_name}({n})", globals=globals(), number=10000)}')


print_timeint('append_left_list', n)
print_timeint('append_left_deque', n)
print_timeint('append_right_list', n)
print_timeint('append_right_deque', n)
print_timeint('pop_left_list', my_list)
print_timeint('pop_left_deque', my_deq)
print_timeint('pop_right_list', my_list)
print_timeint('pop_right_deque', my_deq)
"""
append_left_list 4.6302728
append_left_deque 0.5582171000000002
append_right_list 0.6263875000000008
append_right_deque 0.5385233999999999
pop_left_list 1.4993705000000004
pop_left_deque 0.6285075999999998
pop_right_list 0.5421580000000006
pop_right_deque 0.6070908999999993

По выводу видно что существенно выигрывает deq. Самый лучший результат при добавлении данныс в начало массива 
"""