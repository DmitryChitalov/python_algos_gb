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

# Вывод. Дэк действительно быстрее при аналогичных операциях.

import random
import collections
import timeit


def list_add():
    my_list = [random.randint(1, 100) for i in range(10)]
    my_list.append([random.randint(1, 100) for i in range(10)])
    my_list.insert(0, [random.randint(1, 100) for i in range(10)])
    return my_list


def deque_add():
    my_deque = collections.deque([random.randint(1, 100) for i in range(10)])
    my_deque.append([random.randint(1, 100) for i in range(10)])
    my_deque.appendleft([random.randint(1, 100) for i in range(10)])
    return my_deque


print(list_add())
print(deque_add())

print(timeit.timeit('list_add', setup='from __main__ import list_add', number=10000))
print(timeit.timeit('deque_add', setup='from __main__ import deque_add', number=10000))
