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

test_list = list(i for i in range(10000))
test_deque = deque(i for i in range(10000))

num = 1000


def list_append(num):
    var = list()
    for i in range(num):
        var.append(i)


def deque_append(num):
    var = deque()
    for i in range(num):
        var.append(i)


def deque_appendleft(num):
    var = deque()
    for i in range(num):
        var.appendleft(100)


def list_appendleft(num):
    var = list()
    for i in range(num):
        var.insert(0, 100)


def list_reverse(test_list):
    test_list.reverse()


def deque_reverse(test_deque):
    test_deque.reverse()


def list_get(test_list, num):
    a = test_list[num]


def deque_get(test_deque, num):
    a = test_deque[num]


print(
    f'List append : {timeit(stmt="list_append(1000)",number=10000,globals=globals())} sec'
)
print(
    f'Deque append : {timeit(stmt="deque_append(1000)",number=10000,globals=globals())} sec'
)
print(
    f'List append left: {timeit(stmt="list_appendleft(1000)",number=10000,globals=globals())} sec'
)
print(
    f'Deque append left: {timeit(stmt="deque_appendleft(1000)",number=10000,globals=globals())} sec'
)
print(
    f'List reverse: {timeit(stmt="list_reverse(test_list)",number=10000,globals=globals())} sec'
)
print(
    f'Deque reverse: {timeit(stmt="deque_reverse(test_deque)",number=10000,globals=globals())} sec'
)
print(
    f'List get: {timeit(stmt="list_get(test_list,1000)",number=100000,globals=globals())} sec'
)
print(
    f'Deque get: {timeit(stmt="deque_get(test_deque,1000)",number=100000,globals=globals())} sec'
)

# Обычная встравка работатет в обоих последовательностях одинаково.
# В deque appendleft и reverse работает значительно быстрее чем в list.
# Получение значения по индексу в deque чуть медленне.
