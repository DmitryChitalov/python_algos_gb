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


def list_operations():
    my_list = []
    my_list.append(2)
    my_list.insert(0, 1)
    my_list.pop()
    my_list.pop(0)


def deque_operations():
    my_deque = deque([])
    my_deque.append(2)
    my_deque.appendleft(1)
    my_deque.pop()
    my_deque.popleft()


print(f"list  {timeit('list_operations()', setup='from __main__ import list_operations', number=1000000)}")
print(f"deque {timeit('deque_operations()', setup='from __main__ import deque_operations', number=1000000)}")
