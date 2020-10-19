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


def test_list():
    my_list = list(range(1000))

    my_list.reverse()
    for i in range(1000):
        my_list.pop()
    return True


def test_deque():
    my_deque = deque(range(1000))

    my_deque.reverse()
    for i in range(1000):
        my_deque.pop()
    return True


print(timeit(
    'test_list()',
    'from __main__ import test_list'))  # 104.665599739
print(timeit(
    'test_deque()',
    'from __main__ import test_deque'))  # 102.470977567 - соответствует)

# test_deque()
# test_list()
