"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует действительности.
"""

from timeit import timeit
from collections import deque


def list_append(_list):
    return _list.append(100000)


def list_insert(_list):
    return _list.insert(0, 0)


def list_remove(_list):
    return _list.remove(100000)


def deque_append(_deque):
    return _deque.append(100000)


def deque_append_left(_deque):
    return _deque.appendleft(0)


def deque_remove(_deque):
    return _deque.remove(100000)


my_list = list(range(1, 100000))
my_deq = deque(my_list)

print('Добавление справа')
print(
    timeit(
        "list_append(my_list)",
        setup='from __main__ import list_append, my_list',
        number=10000))
print(
    timeit(
        "deque_append(my_deq)",
        setup='from __main__ import deque_append, my_deq',
        number=10000))
print('Добавление слева')
print(
    timeit(
        "list_insert(my_list)",
        setup='from __main__ import list_insert, my_list',
        number=10000))
print(
    timeit(
        "deque_append_left(my_deq)",
        setup='from __main__ import deque_append_left, my_deq',
        number=10000))
print('Удаление')
print(
    timeit(
        "list_remove(my_list)",
        setup='from __main__ import list_remove, my_list',
        number=10000))
print(
    timeit(
        "deque_remove(my_deq)",
        setup='from __main__ import deque_remove, my_deq',
        number=10000))


"""
Вывод: append показывает себя приблизительно одинаково. 
В случае же с добавлением элемента в начало, deque показывает себя значительно лучше list.
Удаление (я сделал последний элемент, чтобы просмотреть все значения) почему-то у deque занимает в 2 раза больше времени
"""
