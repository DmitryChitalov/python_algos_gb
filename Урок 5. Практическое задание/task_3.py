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
import random

def fill_list(num):
    completed_list = []
    for i in range(num):
        completed_list.append(i)
    return completed_list

def fill_deque(num):
    completed_deque = deque()
    for i in range(num):
        completed_deque.append(i)
    return completed_deque

def random_read_list(_list,tries):
    __readed_item = 0
    __len = len(_list)
    for i in range(tries):
        __readed_item = _list[random.randint(0, __len-1)]

def random_list_deque(_deque,tries):
    __readed_item = 0
    __len = len(_deque)
    for i in range(tries):
        __readed_item = _deque[random.randint(0, __len-1)]

def poping_from_list(_list):
    try:
        while True:
            _list.pop()
    except:
        return 0

def poping_from_deque(_deque):
    try:
        while True:
            _deque.pop()
    except:
        return 0

def poping_first_from_list(_list):
    try:
        while True:
            _list.pop(0)
    except:
        return 0

def poping_first_from_deque(_deque):
    try:
        while True:
            _deque.popleft()
    except:
        return 0

if __name__ == '__main__':
    print(timeit('fill_list(100)', 'from __main__ import fill_list'))
    print(timeit('fill_deque(100)', 'from __main__ import fill_deque'))
    print(timeit('random_read_list(fill_list(100),40)', 'from __main__ import fill_list,random_read_list'))
    print(timeit('random_list_deque(fill_deque(100),40)', 'from __main__ import fill_deque,random_list_deque'))
    print(timeit('poping_from_list(fill_list(200))', 'from __main__ import fill_list,poping_from_list'))
    print(timeit('poping_from_deque(fill_deque(200))', 'from __main__ import fill_deque,poping_from_deque'))
    print(timeit('poping_first_from_list(fill_list(200))', 'from __main__ import fill_list,poping_first_from_list'))
    print(timeit('poping_first_from_deque(fill_deque(200))', 'from __main__ import fill_deque,poping_first_from_deque'))


'''
Заполнение 
4.8324178
4.3607932
Чтение n рандомных элементов по индексу
31.723277
31.9892629
Удаление с хвоста 
17.313904599999987
14.808532900000003
Удаление с головы
24.60842860000001
16.104206599999998

Заполнение и чтение рандомного элемента по индексу одинаковы по времени, при этом удаление с хвоста и головы происходит быстрее у deque

'''
