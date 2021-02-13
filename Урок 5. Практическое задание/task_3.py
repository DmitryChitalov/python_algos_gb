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
"""
2.3800000000004373e-05
9.239999999999943e-05
5.179999999999768e-05
3.3299999999999996e-05
5.140000000000006e-05
4.030000000000006e-05
В простом списке случайный доступ реализован более эффективно,
в очереди методы доступа к первому и последнему элементу
"""
from collections import deque
from random import randint
from timeit import timeit

a_list = []

for i in range(1000):
    a_list.append( i )

a_deque = deque(a_list)
val = 1000
index = randint(0, 1000)
print(
    timeit(
        "a_list[index]",
        setup='from __main__ import a_list, index',
        number=1000))
print(
    timeit(
        "a_list[len(a_list)-1]",
        setup='from __main__ import a_list',
        number=1000))
print(
    timeit(
        "a_list.append(val)",
        setup='from __main__ import a_list, val',
        number=1000))
print(
    timeit(
        "a_deque[index]",
        setup='from __main__ import a_deque, index',
        number=1000))
print(
    timeit(
        "a_deque.appendleft(val)",
        setup='from __main__ import a_deque, val',
        number=1000))
print(
    timeit(
        "a_deque.pop()",
        setup='from __main__ import a_deque',
        number=1000))
