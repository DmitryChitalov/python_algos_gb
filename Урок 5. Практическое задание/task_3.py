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
from timeit import repeat

lst = [0 for i in range(1000)]
dq = deque(0 for i in range(1000))


def lst_append(some_lst):
    for i in range(1000):
        some_lst.append(i)


def deque_append(some_deque):
    for i in range(1000):
        some_deque.append(i)


def lst_left_append(some_lst):
    some_lst.insert(0, 0)


def deque_left_append(some_deque):
    some_deque.appendleft(0)


def lst_pop(some_lst):
    some_lst.pop()


def lst_pop(some_lst):
    some_lst.pop()


def deque_pop(some_deque):
    some_deque.pop()


print('lst_append')
print(min(repeat('lst_append(lst)', globals=globals(), repeat=10, number=1000)))
print('deque_append')
print(min(repeat('deque_append(dq)', globals=globals(), repeat=10, number=1000)))
'''Аппенды примерно одинаковые'''

print('lst_left_append')
print(min(repeat('lst_left_append(lst)', globals=globals(), repeat=10, number=10)))
print('deque_left_append')
print(min(repeat('deque_left_append(dq)', globals=globals(), repeat=10, number=100000)))
"""Подставление в первый элемент намного быстрее в deque"""

print('lst_pop')
print(min(repeat('lst_pop(lst)', globals=globals(), repeat=10, number=1000000)))
print('deque_pop')
print(min(repeat('deque_pop(dq)', globals=globals(), repeat=10, number=1000000)))
"""Обычный pop также одинаков по скорости исполнения"""

"""Логично, что встроенные в deque операции будут проходить быстрее тех, для которых нужны дополнительные команды 
при работе со списками, а методы, синтаксис которых совпадает работают примерно одинакого, концепцию случайного доступа 
не понял"""
