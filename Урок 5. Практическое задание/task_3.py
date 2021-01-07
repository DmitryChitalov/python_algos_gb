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

def append_list():
    my_list = [el for el in range(0, 50)]
    my_list.append(51)

def append_deque():
    simple_lst = list(range(0, 50))
    my_list = deque(simple_lst)
    my_list.append(51)

print(timeit("append_list()", setup="from __main__ import append_list"))
print(timeit("append_deque()", setup="from __main__ import append_deque"))

''' Результаты замеров
 7.6954075
 5.7122494
 Дек работает быстрее
'''
###################################################

def pop_list():
    my_list = [el for el in range(0, 50)]
    my_list.pop()

def pop_deque():
    simple_lst = list(range(0, 50))
    my_list = deque(simple_lst)
    my_list.pop()

print(timeit("pop_list()", setup="from __main__ import pop_list"))
print(timeit("pop_deque()", setup="from __main__ import pop_deque"))

''' Результаты замеров
7.660300100000001
5.702276099999999
Дек работает быстрее
'''
##########################################

def append_list():
    my_list = [el for el in range(0, 50)]
    my_list.insert(0, 1)

def append_left_deque():
    simple_lst = list(range(0, 50))
    my_list = deque(simple_lst)
    my_list.appendleft(1)

print(timeit("append_list()", setup="from __main__ import append_list"))
print(timeit("append_left_deque()", setup="from __main__ import append_left_deque"))

''' Результаты замеров
7.8510925
5.670174299999999
Дек работает быстрее
'''
####################################################################

def del_list():
    my_list = [el for el in range(0, 50)]
    del my_list[0]

def pop_left_deque():
    simple_lst = list(range(0, 50))
    my_list = deque(simple_lst)
    my_list.popleft()

print(timeit("del_list()", setup="from __main__ import del_list"))
print(timeit("pop_left_deque()", setup="from __main__ import pop_left_deque"))

''' Результаты замеров
8.1768721
5.8038126000000005
Дек работает быстрее
'''