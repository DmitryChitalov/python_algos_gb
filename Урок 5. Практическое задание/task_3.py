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

test_lst = [i for i in range(10000)]
test_deque = deque(test_lst)


def lst_append(lst, n):
    temp_lst = lst
    for i in range(n):
        temp_lst.append(i)


def deque_append(deq, n):
    temp_deq = deq
    for i in range(n):
        temp_deq.append(i)


def lst_append_left(lst, n):
    temp_lst = lst
    for i in range(n):
        temp_lst.insert(0, i)


def deque_append_left(deq, n):
    temp_deq = deq
    for i in range(n):
        temp_deq.appendleft(i)


def lst_extend(lst, n):
    temp_lst = lst
    temp_lst.extend([i for i in range(n)])


def deque_extend(deq, n):
    temp_deq = deq
    temp_deq.extend([i for i in range(n)])


def lst_pop(lst):
    temp_lst = lst
    for i in range(len(temp_lst)):
        temp_lst.pop()


def deque_pop(deq):
    temp_deq = deq
    for i in range(len(temp_deq)):
        temp_deq.pop()


def lst_access(lst):
    for i in lst:
        a = i

def deque_access(deq):
    for i in deq:
        a = i


print('=== append ===')
print(timeit("lst_append(test_lst, 1000)",
             number=1000,
             globals=globals()))
print(timeit("deque_append(test_deque, 1000)",
             number=1000,
             globals=globals()))
print('=== append left ===')
print(timeit("lst_append_left(test_lst, 10)",
             number=1000,
             globals=globals()))
print(timeit("deque_append_left(test_deque, 10)",
             number=1000,
             globals=globals()))
print('=== extend ===')
print(timeit("lst_extend(test_lst, 100)",
             number=1000,
             globals=globals()))
print(timeit("deque_extend(test_deque, 100)",
             number=1000,
             globals=globals()))
print('=== pop ===')
print(timeit("lst_pop(test_lst)",
             number=1000,
             globals=globals()))
print(timeit("deque_pop(test_deque)",
             number=1000,
             globals=globals()))
print('=== access ===')
print(timeit("lst_access(test_lst)",
             number=1000,
             globals=globals()))
print(timeit("deque_access(test_deque)",
             number=1000,
             globals=globals()))

#по результатам замеров функции расширения и добавления в деке работают быстрее
#особенно слева (т.к. для списка встроенной функции нет), доступ к элементам
# списка получается незначительно быстрее
