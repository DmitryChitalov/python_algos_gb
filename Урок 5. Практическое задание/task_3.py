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

foo = 1000
lst_1 = [el for el in range(1000)]
dq_1 = deque(lst_1)

#************************************ LIST **********************************************
def append_lst(num):
    '''
    Добавляет элемент в конец списка
    '''
    my_list = []
    for i in range(num):
        my_list.append(i)
    return my_list

def append_left_lst(num):
    '''
    Добавляет элемент в начало списка (appendleft)
    '''
    my_list = []
    for i in range(num):
        my_list.insert(0, i)
    return my_list

def extend_lst(lst_1):
    '''
    Добавляет в конец все элементы lst.
    '''
    my_list = []
    my_list.extend(lst_1)
    return my_list

def extend_left_lst(lst_1):
    '''
    Добавляет в начало все элементы lst.
    '''
    my_list = []
    for el in lst_1:
        my_list.insert(0, el)
    return my_list

def pop_lst(lst_1):
    '''
    Удаляет и возвращает последний элемент очереди
    '''
    for i in range(len(lst_1)):
        return lst_1.pop()

def pop_left_lst(lst_1):
    '''
    Удаляет и возвращает первый элемент очереди
    '''
    for i in range(len(lst_1)):
        return lst_1.pop(0)

def lst_reverse(lst_1):
    '''
    Разворачивает очередь
    '''
    lst_1.reverse()
    return lst_1

#************************************ DEQUE **********************************************
def append_dq(num):
    '''
    Добавляет num в конец
    '''
    my_list = deque()
    for i in range(num):
        my_list.append(i)
    return my_list

def append_left_dq(num):
    '''
    Добавляет num в начало
    '''
    my_list = deque()
    for i in range(num):
        my_list.appendleft(i)
    return my_list

def extend_dq(lst_1):
    '''
    Добавляет в конец все элементы lst_1
    '''
    my_list = deque()
    my_list.extend(lst_1)
    return my_list

def extend_left_dq(lst_1):
    '''
    добавляет в начало все элементы lst_1 (начиная с последнего элемента lst_1).
    '''
    my_list = deque()
    my_list.extendleft(lst_1)
    return my_list

def pop_dq(lst_1):
    '''
    Удаляет и возвращает последний элемент очереди
    '''
    for i in range(len(lst_1)):
        return lst_1.pop()

def pop_left_dq(lst_1):
    '''
    Удаляет и возвращает первый элемент очереди
    '''
    for i in range(len(lst_1)):
        return lst_1.popleft()

def reverse_dq(lst_1):
    '''
    Разворачивает очередь
    '''
    lst_1.reverse()
    return lst_1

print(timeit.timeit('append_lst(foo)', setup="from __main__ import append_lst, foo", number=10000))
print(timeit.timeit('append_dq(foo)', setup="from __main__ import append_dq, foo", number=10000))

print(timeit.timeit('append_left_lst(foo)', setup="from __main__ import append_left_lst, foo", number=10000))
print(timeit.timeit('append_left_dq(foo)', setup="from __main__ import append_left_dq, foo", number=10000))

print(timeit.timeit('extend_lst(lst_1)', setup="from __main__ import extend_lst, lst_1", number=10000))
print(timeit.timeit('extend_dq(lst_1)', setup="from __main__ import extend_dq, lst_1", number=10000))

print(timeit.timeit('extend_left_lst(lst_1)', setup="from __main__ import extend_left_lst, lst_1", number=10000))
print(timeit.timeit('extend_left_dq(lst_1)', setup="from __main__ import extend_left_dq, lst_1", number=10000))

print(timeit.timeit('pop_lst(lst_1)', setup="from __main__ import pop_lst, lst_1", number=10000))
print(timeit.timeit('pop_dq(lst_1)', setup="from __main__ import pop_dq, lst_1", number=10000))

print(timeit.timeit('pop_left_lst(lst_1)', setup="from __main__ import pop_left_lst, lst_1", number=10000))
print(timeit.timeit('pop_left_dq(lst_1)', setup="from __main__ import pop_left_dq, lst_1", number=10000))

print(timeit.timeit('lst_reverse(lst_1)', setup="from __main__ import lst_reverse, lst_1", number=10000))
print(timeit.timeit('reverse_dq(lst_1)', setup="from __main__ import reverse_dq, lst_1", number=10000))
'''
    Добавляет элемент в конец списка
List -  1.3680338
Deque - 1.2068556
    Добавляет элемент в начало списка (append_left)
List -  4.5061072
Deque - 1.2114519999999995
    Добавляет в конец все элементы lst. (extend)
List -  0.023471100000000078
Deque - 0.08496710000000007
    Добавляет в начало все элементы lst. (extend_left)
List -  4.041851399999999
Deque - 0.08255260000000142
    Удаляет и возвращает последний элемент очереди (pop)
List -  0.005035899999999316
Deque - 0.004667500000000047
    Удаляет и возвращает первый элемент очереди (pop_left)
List -  0.004705099999998907
Deque - 0.004812199999999933
    Разворачивает очередь   (reverse)
List -  0.0017590999999992363
Deque - 0.001956899999999706
'''

# Как мы видим из результатов в deque быстрее выполняется append слева и extend слева
