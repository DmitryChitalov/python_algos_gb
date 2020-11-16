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

from random import randint
from collections import deque
from timeit import timeit


my_list = [randint(1, 100) for i in range(1, 20)]
my_deque = deque(my_list)


# lst functions:

def list_func_1(lst):
    new_my_list = []
    for i in range(len(lst)):
        new_my_list.append(lst[i] ** 2)
    return new_my_list

def list_func_2(lst):
    return max(lst, key=lst.count)

def list_func_3(lst):
    new_my_list = []
    for i in range(len(lst)):
        lst[i] //= 3
        new_my_list.insert(1, lst[i])
        return new_my_list


print('Time measures of list functions:')
print(round(timeit('list_func_1(my_list)', 'from __main__ import list_func_1, my_list', number=100000), 2))
print(round(timeit('list_func_2(my_list)', 'from __main__ import list_func_2, my_list', number=100000), 2))
print(round(timeit('list_func_3(my_list)', 'from __main__ import list_func_3, my_list', number=100000), 2))


# deque functions:

def deque_func_1(deq):
    new_my_deque = deque()
    for i in range(len(deq)):
        new_my_deque.append(deq[i] ** 2)
    return new_my_deque

def deque_func_2(deq):
    return max(deq, key=deq.count)

def deque_func_3(deq):
    new_my_deque = []
    for i in range(len(deq)):
        deq[i] //= 3
        new_my_deque.insert(1, deq[i])
        return new_my_deque


print('Time measures of deque functions:')
print(round(timeit('deque_func_1(my_deque)', 'from __main__ import deque_func_1, my_deque', number=100000), 2))
print(round(timeit('deque_func_2(my_deque)', 'from __main__ import deque_func_2, my_deque', number=100000), 2))
print(round(timeit('deque_func_3(my_deque)', 'from __main__ import deque_func_3, my_deque', number=100000), 2))


# to sum up:
'''
В случае использованных мною функций вышло так, что только первая функция - построенная на append'е - показала существенную
разницу во времени исполнения: deque выиграл во времени у list (напр. 1.46 vs 1.05), что, по всей видимости, соответствует 
документации. В случае max() и insert() разницы фактически не было, исполнялись функции одинаково. 
'''




