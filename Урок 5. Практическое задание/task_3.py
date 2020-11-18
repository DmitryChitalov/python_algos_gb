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
"""Проведя замеры различных операций выяснил, что
У deque операция append работает медленнее, чем у простого списка
операция insert в простом списке ОЧЕНЬ медленная (в 50 раз медленнее append и appendleft
операция pop у простого списка медленнее, чем у deque. А у deque popleft быстрее pop.
"""

from collections import deque
from timeit import timeit


def func_1():
    simple_list = []
    for i in range(10000):
        simple_list.append(i)
    return simple_list


def func_2():
    deque_list = deque()
    for i in range(10000):
        deque_list.append(i)
    return deque_list


def func_3():
    simple_list = []
    for i in range(10000):
        simple_list.insert(0, i)
    return simple_list


def func_4():
    deque_list = deque()
    for i in range(10000):
        deque_list.appendleft(i)
    return deque_list


def func_5():
    simple_list = []
    for i in range(10000):
        simple_list.append(i)
        simple_list.pop()
    return simple_list


def func_6():
    deque_list = deque()
    for i in range(10000):
        deque_list.append(i)
        deque_list.popleft()
    return deque_list


def func_7():
    deque_list = deque()
    for i in range(10000):
        deque_list.append(i)
        deque_list.pop()
    return deque_list


functions = ["func_1()", "func_2()", "func_3()", "func_4()", "func_5()", "func_6()", "func_7()"]
setup_data = "from __main__ import func_1, func_2, func_3, func_4, func_5, func_6, func_7"

for fn in functions:
    print(f'Время выполнения функции {fn}',
          timeit(fn, setup=setup_data, number=10))
