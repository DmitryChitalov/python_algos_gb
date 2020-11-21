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


def simple_list():
    my_list = list(range(100))
    my_list.append(1)
    my_list.insert(-1, 0)
    my_list.pop(0)
    my_list.pop()


def deq():
    my_deque = deque(range(100))
    my_deque.append(1)
    my_deque.appendleft(-1)
    my_deque.pop()
    my_deque.popleft()


print(timeit(stmt='simple_list', setup='from __main__ import simple_list'))
print(timeit(stmt='deq', setup='from __main__ import deq'))

# разницу в скорости я не заметил