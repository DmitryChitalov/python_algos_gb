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

num = 100
list = [el for el in range(10000000)]


def list_append(num):
    list1 = []
    for i in range(num):
        list1.append(i)

def deque_append(num):
    list1 = deque()
    for i in range(num):
        list1.append(i)

def list_appendleft(num):
    list1 = []
    for i in range(num):
        list1.insert(0, i)

def deque_appendleft(num):
    list1 = deque()
    for i in range(num):
        list1.appendleft(i)

def list_pop(list1):
    for i in range(len(list1)):
        a = list1.pop()

def deque_pop(list1):
    for i in range(len(list1)):
        l = list1.pop()


def list_popleft(list1):
    for i in range(len(list1)):
        l = list1.pop(0)


def deque_popleft(list1):
    for i in range(len(list1)):
        l = list1.popleft()



print('list_append -',
    timeit(
        'list_append(num)', globals=globals(), number=100000))
deque_append(num)
print('deque_append -',
    timeit(
        'deque_append(num)', globals=globals(), number=100000))
print('list_appendleft -',
    timeit(
        'list_appendleft(num)', globals=globals(), number=100000))
print('deque_appendleft -',
    timeit(
        'deque_appendleft(num)', globals=globals(), number=100000))
print('list_pop -',
    timeit(
        'list_pop(list)', globals=globals(), number=1000000))
print('deque_pop -',
    timeit(
        'deque_pop(list)', globals=globals(), number=1000000))
print('list_popleft -',
    timeit(
        'list_popleft(list)', globals=globals(), number=10000000))
print('deque_popleft -',
    timeit(
        'deque_popleft(list)', globals=globals(), number=10000000))

'''
List отрабатывает на равне с deque в append, pop_left. Deque на много лучше показал себя в append_left, pop 

list_append - 0.8490065
deque_append - 0.7456488999999997

list_appendleft - 1.3975592
deque_appendleft - 0.7122562000000006

list_pop - 1.8785327
deque_pop - 0.4482677000000006

list_popleft - 4.317518300000001
deque_popleft - 4.3892772
'''
