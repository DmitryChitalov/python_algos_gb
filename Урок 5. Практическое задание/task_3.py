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

def deque_appendleft():
    d = deque()
    for i in range(10000):
        d.appendleft(i)
""" 0.10855882 """

def list_insert():
    l = list()
    for i in range(10000):
        l.insert(0,i)
""" 4.034820783 """
"""Операция вставки слева у deque выполняется примерно в 40 раз быстрее, чем в list"""


def deque_append():
    d = deque()
    for i in range(10000):
        d.append(i)
""" 1.079918409 """

def list_append():
    l = list()
    for i in range(10000):
        l.append(i)
""" 1.0754786400000003 """
"""Операция вставки справа у list и deque выполняется примерно одинаково, 
но у списка всё же немного быстрее(на тысячные доли секунд)"""

def deque_popleft():
    d = deque(range(1000))
    for i in range(len(d)):
        d.popleft()
""" 1.103089159 """

def list_popleft():
    l = list(range(1000))
    for i in range(len(l)):
        l.pop(0)
""" 3.4533737010000003 """
"""Операция удаления слева у deque происходит примерно в 3 раза быстрее, чем у list"""

def deque_pop():
    d = deque(range(10000))
    for i in range(len(d)):
        d.pop()
""" 12.219730597 """

def list_pop():
    l = list(range(10000))
    for i in range(len(l)):
        l.pop()
""" 11.1420377170 """
"""Операция удаления справа у deque немного медленнее, чем у list"""

def deque_insert():
    d = deque()
    for i in range(10000):
        d.insert(0,i)
""" 0.179977935 """

def list_insert():
    l = list()
    for i in range(10000):
        l.insert(0,i)
""" 4.120569081999999 """
"""Операция вставки слева(insert) у deque выполняется также в 40 раз быстрее, чем в list"""

print("deque_appendleft: ",timeit.timeit("deque_appendleft()","from __main__ import deque_appendleft",number=100))
print("list_appendleft: ",timeit.timeit("list_insert()","from __main__ import list_insert",number=100))

print("deque_append: ",timeit.timeit("deque_append()","from __main__ import deque_append",number=1000))
print("list_append: ",timeit.timeit("list_append()","from __main__ import list_append",number=1000))

print("deque_popleft: ",timeit.timeit("deque_popleft()","from __main__ import deque_popleft",number=10000))
print("list_popleft:",timeit.timeit("list_popleft()","from __main__ import list_popleft",number=10000))

print("deque_pop: ",timeit.timeit("deque_pop()","from __main__ import deque_pop",number=1000))
print("list_pop: ",timeit.timeit("list_pop()","from __main__ import list_pop",number=1000))

print("deque_insert: ", timeit.timeit("deque_insert()","from __main__ import deque_insert",number=100))
print("list_insert: ",timeit.timeit("list_insert()","from __main__ import list_insert",number=100))

""" Конечный вывод:
deque_appendleft:  0.10792662
list_appendleft:  4.087402694000001
deque_append:  1.1247040410000002
list_append:  1.1050257860000006
deque_popleft:  1.0626375880000003
list_popleft: 3.418373829000001
deque_pop:  1.2589813979999995
list_pop:  1.5526173189999994
deque_insert:  0.1841313669999991
list_insert:  3.9343697239999997

Вывод: у deque операции и удаления в начало сложность равна O(1) - согласно различным статьям на различных сайтах
, а у списка обратная ситуация: вставка/удалиние в/из начала имеет сложность O(n), 
но в операциях по извлечению значения(случайный доступ), у списка происходит быстрее чем в deque.
"""