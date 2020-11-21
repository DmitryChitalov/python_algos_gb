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
import timeit

list_range = [el for el in range(1000)]
deque_range = deque ()
deque_range.extend(list_range)

def list_add(el):
    list = []
    for i in range(el):
        list.append(i)

def list_add_left(el):
    list = []
    for i in range(el):
        list.insert(0, i)

def list_ext(list_range):
    list = []
    list.extend(list_range)

def deque_add(el):
    list = deque()
    for i in range(el):
        list.append(i)

def deque_ext(list_range):
    list = deque()
    list.extend(list_range)

def deque_add_left(el):
    list = deque()
    for i in range(el):
        list.appendleft(i)



