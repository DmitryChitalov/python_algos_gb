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
import random

setup = """
import collections as coll
import random


list1 = [random.choice(range(1001)) for _ in range(10000)]
deque = coll.deque([random.choice(range(1001)) for _ in range(10000)])


def sum_first_last(some_list, n):
    res = 0
    for _ in range(n):
        try:
            res += (some_list.pop() + some_list.popleft())
        except AttributeError:
            res += (some_list.pop() + some_list.pop(0))
    return res


def sum_random(some_list, n):
    res = 0
    for _ in range(n):
        rand = random.choice(range(len(some_list) - 1))
        res += some_list[rand]
        del some_list[rand]
    return res


n = 234
"""

check_list = 'sum_first_last(list1, n)'
check_deque = 'sum_first_last(deque, n)'
check2_list = 'sum_random(list1, n)'
check2_deque = 'sum_random(deque, n)'
print('Время выполнения суммы n чисел с начала и конца: ')
print(f'Время выполнения списка - {timeit(check_list, setup, number=10)}')
print(f'Время выполнения колоды - {timeit(check_deque, setup, number=10)}')

print('Время выполнения суммы n случайных чисел: ')
print(f'Время выполнения списка - {timeit(check2_list, setup, number=10)}')
print(f'Время выполнения колоды - {timeit(check2_deque, setup, number=10)}')



