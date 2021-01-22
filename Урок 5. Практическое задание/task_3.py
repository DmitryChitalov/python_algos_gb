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

simple_list = [42, 43, 443]
simple_deque = deque([31, 56, 201])


def one():
    simple_list.append(45)


def one_dec():
    simple_deque.append(45)


def two():
    simple_list.insert(0, 45)


def two_dec():
    simple_deque.appendleft(45)


def three():
    return simple_list[2]


def three_dec():
    return simple_deque[2]


print(timeit('one()', 'from __main__ import one, simple_list', number=1000))
print(timeit('two()', 'from __main__ import two, simple_list', number=1000))
print(timeit('three()', 'from __main__ import three, simple_list', number=1000))
print(timeit('one_dec()', 'from __main__ import one_dec, simple_deque', number=1000))
print(timeit('two_dec()', 'from __main__ import two_dec, simple_deque', number=1000))
print(timeit('three_dec()', 'from __main__ import three_dec, simple_deque', number=1000))


"""
Результаты:
Список
0.00010939999999999908
0.0006862000000000014
7.619999999999849999

Дека
0.0001105999999999989
0.00011309999999999792
8.989999999999693333

Вывод:
При использовании простого списка, доступ к элементу по индексу быстрее, чем через деку, однако
при вставке элмента, значение времени на insert по нулевому индексу больше, 
чем на appendleft из модуля деки.
Вставка в конец списка практически одинаковая.
Все согласно документации.
"""

