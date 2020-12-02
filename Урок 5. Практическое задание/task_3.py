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

def fun_append_list():
    my_list = [el for el in range(0, 10)]
    my_list.append(11)

def fun_append_deque():
    simple_lst = list("0123456789")
    my_list = deque(simple_lst)
    my_list.append(11)

print(timeit("fun_append_list()", setup="from __main__ import fun_append_list"))
print(timeit("fun_append_deque()", setup="from __main__ import fun_append_deque"))

''' Результаты замеров
0.9264530240000001
0.648602546
Дек справляется быстрее
'''

def fun_pop_list():
    my_list = [el for el in range(0, 10)]
    my_list.pop(9)

def fun_pop_deque():
    simple_lst = list("0123456789")
    my_list = deque(simple_lst)
    my_list.pop()

print(timeit("fun_pop_list()", setup="from __main__ import fun_pop_list"))
print(timeit("fun_pop_deque()", setup="from __main__ import fun_pop_deque"))

''' Результаты замеров
0.8974727680000001
0.6441470709999999
Дек справляется быстрее
'''
def fun_appendleft_list():
    my_list = [el for el in range(0, 10)]
    my_list.insert(0, 1)

def fun_appendleft_deque():
    simple_lst = list("0123456789")
    my_list = deque(simple_lst)
    my_list.appendleft(1)

print(timeit("fun_appendleft_list()", setup="from __main__ import fun_appendleft_list"))
print(timeit("fun_appendleft_deque()", setup="from __main__ import fun_appendleft_deque"))

''' Результаты замеров
0.9169307010000001
0.6609186490000001
Дек справляется быстрее
'''
