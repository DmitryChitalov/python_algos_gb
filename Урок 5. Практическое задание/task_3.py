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

#append(value) - добавляет value в конец.
def list_append(value):
    my_list = []
    for i in range(value):
        my_list.append(i)


def deque_append(value):
    my_list = deque()
    for i in range(value):
        my_list.append(i)

# pop() - удаляет и возвращает последний элемент очереди.
def list_pop(list_range):
    for i in range(len(list_range)):
        res = list_range.pop()


def deque_pop(list_range):
    for i in range(len(list_range)):
        res = list_range.pop()


val_1 = 10111
val_2 = [el for el in range(101011)]


print('list_append = ',timeit("list_append(val_1)",setup="from __main__ import list_append, val_1",number=10000))

print('deque_append = ',timeit("deque_append(val_1)",setup="from __main__ import deque_append, val_1",number=10000))

print('list_pop = ',timeit("list_pop(val_2)",setup="from __main__ import list_pop, val_2",number=10000))

print('deque_pop = ',timeit("deque_pop(val_2)",setup="from __main__ import deque_pop, val_2",number=10000))

