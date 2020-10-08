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


def add_el(array):
    array.append(11)


def del_el(array):
    array.pop()


def del_left_el_list(array):
    array.pop(0)


def del_left_el_deque(array):
    array.popleft()


def get_el(array):
    result = array[10]


my_list = [x for x in range(1_000_000)]
my_deque = deque(my_list)

print(timeit("add_el(my_list)", setup="from __main__ import add_el, my_list", number=100_000))  # -> 0.030
print(timeit("add_el(my_deque)", setup="from __main__ import add_el, my_deque", number=100_000))  # -> 0.025

print(timeit("del_el(my_list)", setup="from __main__ import del_el, my_list", number=100_000))  # -> 0.023
print(timeit("del_el(my_deque)", setup="from __main__ import del_el, my_deque", number=100_000))  # -> 0.018

print(timeit("del_left_el_list(my_list)", setup="from __main__ import del_left_el_list, my_list",
             number=100_000))  # -> 57.950
print(timeit("del_left_el_deque(my_deque)", setup="from __main__ import del_left_el_deque, my_deque",
             number=100_000))  # -> 0.027

print(timeit("get_el(my_list)", setup="from __main__ import get_el, my_list", number=100_000))  # -> 0.015
print(timeit("get_el(my_deque)", setup="from __main__ import get_el, my_deque", number=100_000))  # -> 0.017

""" Стандартные операции удаления/добавления с деком быстрее, 
    удаление слева быстрее в тысячи раз,
    получение элементов быстрее у списка.
    информация в документации соответствует дейстивтельности."""