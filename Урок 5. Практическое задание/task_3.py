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
from random import randint
from timeit import timeit


def append_list():
    for i in range(100):
        j = randint(1, 1000)
        var_list.append(j)


def append_deq():
    for i in range(100):
        j = randint(1, 1000)
        var_deq.append(j)


def insert_list_5():
    j = randint(1, 1000)
    var_list.insert(5, j)


def insert_deq_5():
    j = randint(1, 1000)
    var_deq.insert(5, j)


def pop_list():
    j = var_list.pop()


def pop_deq():
    j = var_deq.pop()


def revers_list():
    var_list.reverse()


def revers_deq():
    var_deq.reverse()


def insert_list_1():
    j = randint(1, 1000)
    var_list.insert(1, j)


def append_left_deq():
    j = randint(1, 1000)
    var_deq.appendleft(j)


var_list = list()
var_deq = deque()

print('append_list:\t', timeit("append_list()",
                               setup="from __main__ import append_list",
                               number=10000))
print('append_deq:\t', timeit("append_deq()",
                              setup="from __main__ import append_deq",
                              number=10000))

print('----------------------------------')
print('insert_list_5:\t',
      timeit("insert_list_5()", setup="from __main__ import insert_list_5",
             number=10000))
print('insert_deq_5:\t',
      timeit("insert_deq_5()", setup="from __main__ import insert_deq_5",
             number=10000))

print('----------------------------------')
print('pop_list:\t',
      timeit("pop_list()", setup="from __main__ import pop_list",
             number=10000))
print('pop_deq:\t',
      timeit("pop_deq()", setup="from __main__ import pop_deq",
             number=10000))

print('----------------------------------')
print('revers_list:\t',
      timeit("revers_list()", setup="from __main__ import revers_list",
             number=10000))
print('revers_deq:\t',
      timeit("revers_deq()", setup="from __main__ import revers_deq",
             number=10000))

print('----------------------------------')
print('insert_list_1:\t',
      timeit("insert_list_1()", setup="from __main__ import insert_list_1",
             number=10000))
print('append_left_deq:\t',
      timeit("append_left_deq()", setup="from __main__ import append_left_deq",
             number=10000))

#
# append_list:	 2.0979442
# append_deq:	 2.0082067
# Заполнение списка и дека выполняется практически одинаково
# ----------------------------------
# insert_list_5:	 12.7179334
# insert_deq_5:	 0.021652400000000682
# операция insert в позицию 5 в деке выполняется гораздо быстрее
# ----------------------------------
# pop_list:	 0.0019354000000006977
# pop_deq:	 0.002358799999999661
# получение элемента через pop выполняется практически одинаково
# ----------------------------------
# revers_list:	 12.948276
# revers_deq:	 19.2171737
# реверc у списка выполняется быстрее
# ----------------------------------
# insert_list_1:	 12.603372199999995
# append_left_deq:	 0.023299999999998988
# вставка элемента слева у дека выполняется быстрее, чем у списка
