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
from random import random
from timeit import timeit

list_l = ['a', 2, 343.2, 'ba', 2343, 2, 343.2]
d = deque(list_l) 
rand = random()

def list_tries():
    lst = list_l.append(rand)
    lst = list_l.insert(0, rand)
    lst_c = list_l.count(2)
    lst = list_l.pop()
    lst = list_l.pop(0)
    for elem in list_l:
        return elem
    return list_l

def deque_tries():
    deque_ap = d.append('good')
    deque_apl = d.appendleft(10020)
    deque_c = d.count(343.2)
    deque_p = d.pop()
    deque_pl = d.popleft()
    for elem in d:
        return elem
    return d

#print(list_tries())
#print(deque_tries())

print(timeit("list_tries()", setup="from __main__ import list_tries, list_l", number=1000))   # 0.0008112799999999976
print(timeit("deque_tries()", setup="from __main__ import deque_tries, d", number=1000)) # 0.000703556000000001


""" Проведя замеры можно увидеть, что deque, работает быстрее чем list """