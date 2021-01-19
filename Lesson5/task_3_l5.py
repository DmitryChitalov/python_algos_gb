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


def append_list(n):
    my_list = []
    for i in range(n):
        my_list.append(randint(0, 5))
    return my_list


def append_deque(n):
    my_deque = deque()
    for i in range(n):
        my_deque.append(randint(0, 5))
    return my_deque


def insert_my_list():
    my_list.insert(0, 7)

def appendleft_my_deque():
    my_deque.appendleft(7)

def pop_list(my_list):
    my_list.pop()
    return my_list

def pop_deque(my_deque):
    my_deque.pop()
    return my_deque

def the_list():
    return my_list[5]

def the_deque():
    return my_deque[5]

n = 100
my_list = [i for i in range(777)]
my_deque = deque(my_list)
print("Время заполнения ")
print(timeit("append_list(n)", setup="from __main__ import append_list, n", number=1000))
print(timeit("append_deque(n)", setup="from __main__ import append_deque, n", number=1000))
print("Время добавления элемента (.insert и .appendleft) ")
print(timeit('insert_my_list()', 'from __main__ import insert_my_list, my_list', number=1000))
print(timeit('appendleft_my_deque()', 'from __main__ import appendleft_my_deque, my_deque', number=1000))
print("Время удаления элементa (.pop) ")
print(timeit("pop_list(my_list)", setup="from __main__ import pop_list, my_list", number=1000))
print(timeit("pop_deque(my_deque)", setup="from __main__ import pop_deque, my_deque", number=1000))
print("Время обращения к элементу ")
print(timeit('the_list()', 'from __main__ import the_list, my_list', number=10000))
print(timeit('the_deque()', 'from __main__ import the_deque, my_deque', number=10000))

"""
"""
"""
Результаты сравнения list и deque соответственно:

Время заполнения 
0.268151365
0.258063423
Время добавления элемента (.insert и .appendleft)   #самая заметная разница!
0.0013138769999999633
0.0003141289999999408
Время удаления элементa (.pop) 
0.0003002699999999914
0.0002941109999999858
Время обращения к элементу 
0.0022739729999999847
0.0023174740000000416

Результаты замеров подтверждают, что добавление и извлечение элементов в deque работает быстрее. Однако время
доступа к случайному элементу в деке несколько больше, чем в списке

"""

