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

list = [el for el in range(10000)]
n_deque = deque(list)


# append(num) - добавляет num в конец.

def list_append(num):
    list = []
    for i in range(num):
        list.append(i)


def deque_append(num):
    list = deque()
    for i in range(num):
        list.append(i)


# appendleft(num) - добавляет num в начало, то же самое делает insert(0,i) - добавляет на 0 позицию элемент

def list_appendleft(num):
    list = []
    for i in range(num):
        list.insert(0, i)


def deque_appendleft(num):
    list = deque()
    for i in range(num):
        list.appendleft(i)


# extend(iterable) - добавляет в конец все элементы iterable.
def list_extend(list_iterable):
    list = []
    list.extend(list_iterable)


def deque_extend(list_iterable):
    list = deque()
    list.extend(list_iterable)


# extendleft(iterable) - добавляет в начало все элементы iterable (начиная с последнего элемента iterable).
def list_extendleft(list_iterable):
    list = []
    for i in list_iterable:
        list.insert(0, i)


def deque_extendleft(list_iterable):
    list = deque()
    list.extendleft(list_iterable)


# pop() - удаляет и возвращает последний элемент очереди.

def list_pop(list_iterable):
    for i in range(len(list_iterable)):
        elem = list_iterable.pop()


def deque_pop(list_iterable):
    for i in range(len(list_iterable)):
        elem = list_iterable.pop()


# reverse() - разворачивает очередь.
def list_reverse(list_iterable):
    elem = list_iterable.reverse()


def deque_reverse(list_iterable):
    elem = list_iterable.reverse()


# remove(num) - удаляет первое вхождение num.

def list_remove(list_iterable):
    elem = list_iterable.remove(100)


def deque_remove(list_iterable):
    elem = list_iterable.remove(100)

#clear() - очищает очередь.
def list_clear(list_iterable):
    elem = list_iterable.clear()



def deque_clear(list_iterable):
    elem = list_iterable.clear()



name_list = 'list_append deque_append list_appendleft deque_appendleft list_extend deque_extend list_extendleft deque_extendleft list_pop deque_pop list_reverse deque_reverse list_remove deque_remove list_clear deque_clear'.split()

num_time = 100

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print()
    if id <= 3:
        print(
            f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=num_time)}")
    else:
        if id % 2 == 0:
            print(
                f"{func_name}(list) -\t{timeit.timeit(stmt=func_name + f'({list})', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
        else:
            print(
                f"{func_name}(n_deque) -\t{timeit.timeit(stmt=func_name + f'({n_deque})', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")

"""
print(timeit.timeit("list_append(num)", setup="from __main__ import list_append"))

print(timeit.timeit("deque_append(num)", setup="from __main__ import deque_append"))


Методы, определённые в deque:

append(x) - добавляет x в конец.

appendleft(x) - добавляет x в начало.

clear() - очищает очередь.

count(x) - количество элементов, равных x.

extend(iterable) - добавляет в конец все элементы iterable.

extendleft(iterable) - добавляет в начало все элементы iterable (начиная с последнего элемента iterable).

pop() - удаляет и возвращает последний элемент очереди.

popleft() - удаляет и возвращает первый элемент очереди.

remove(value) - удаляет первое вхождение value.

reverse() - разворачивает очередь.

rotate(n) - последовательно переносит n элементов из начала в конец (если n отрицательно, то с конца в начало).

"""
