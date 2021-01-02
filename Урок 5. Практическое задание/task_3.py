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

my_list = []
my_deque = deque()


def list_append(used_list):
    for i in range(10000):
        used_list.append(i)


def deque_append(used_deque):
    for i in range(10000):
        used_deque.append(i)


def append_left_list(used_list):
    for i in range(10):
        used_list.insert(0, i)


def append_left_deque(used_deque):
    for i in range(10):
        used_deque.appendleft(i)


def rotate_list(used_list):
    for i in range(10):
        used_list[-1], used_list[0] = used_list[0], used_list[-1]


def rotate_deque(used_deque):
    used_deque.rotate(10)


print(
    f'Заполнение для списка: {timeit("list_append(my_list)", setup="from __main__ import list_append, my_list", number=1000)}')
print(
    f'Заполнение для дека: {timeit("deque_append(my_deque)", setup="from __main__ import deque_append, my_deque", number=1000)}')
print(
    f'Заполнение для списка слева: {timeit("append_left_list(my_list)", setup="from __main__ import append_left_list, my_list", number=100)}')
print(
    f'Заполнение для дека слева: {timeit("append_left_deque(my_deque)", setup="from __main__ import append_left_deque, my_deque", number=100)}')
print(
    f'Перемещение 10 элементов в начало для списка: {timeit("rotate_list(my_list)", setup="from __main__ import rotate_list, my_list")}')
print(
    f'Перемещение 10 элементов в начало для дека: {timeit("rotate_deque(my_deque)", setup="from __main__ import rotate_deque, my_deque")}')


"""
Заполнение для списка: 0.8075861
Заполнение для дека: 0.6677374
Заполнение для списка слева: 4.7582084
Заполнение для дека слева: 8.21000000001959e-05
Перемещение 10 элементов в начало для списка: 1.1550776000000003
Перемещение 10 элементов в начало для дека: 0.15145889999999973
Вывод: Добавление и перемещении элемента в начало или конец в deque происходит гораздо быстрее чем в списке"""