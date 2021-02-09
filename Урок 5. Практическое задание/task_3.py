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
from random import choice
from string import ascii_lowercase
from timeit import timeit


def ins_deque():
    dq = deque('abc')
    letters = ascii_lowercase
    for i in range(5000):
        dq.append(choice(letters))


def ins_list():
    ls = list('abc')
    letters = ascii_lowercase
    for i in range(5000):
        ls.append(choice(letters))


def pop_deque():
    dq = deque('abc')
    letters = ascii_lowercase
    for i in range(5000):
        dq.append(choice(letters))
    for i in range(5000):
        dq.pop()


def pop_list():
    ls = list('abc')
    letters = ascii_lowercase
    for i in range(5000):
        ls.append(choice(letters))
    for i in range(5000):
        ls.pop()


def get_deque():
    dq = deque('abc')
    letters = ascii_lowercase
    for i in range(5000):
        dq.append(choice(letters))
    for i in range(5000):
        bb = dq[i]


def get_list():
    ls = list('abc')
    letters = ascii_lowercase
    for i in range(5000):
        ls.append(choice(letters))
    for i in range(5000):
        bb = ls[i]


print('ins_deque()', timeit('ins_deque()', setup='from __main__ import ins_deque', number=1000))
print('pop_deque()', timeit('pop_deque()', setup='from __main__ import pop_deque', number=1000))
print('get_deque()', timeit('get_deque()', setup='from __main__ import get_deque', number=1000))
print('ins_list()', timeit('ins_list()', setup='from __main__ import ins_list', number=1000))
print('pop_list()', timeit('pop_list()', setup='from __main__ import pop_list', number=1000))
print('get_list()', timeit('get_list()', setup='from __main__ import get_list', number=1000))
# Документация не совсем корректна: дека быстрее листа получается.
# Причем для всех операций.
