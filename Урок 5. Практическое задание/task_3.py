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
from random import randint
from timeit import timeit


def list_append(lst):
    for i in range(100):
        lst.append(99)
    return lst


def list_insert_left(lst):
    for i in range(100):
        lst.insert(0, 99)
    return lst


def list_insert_random(lst):
    for i in range(100):
        rand = randint(0, 100)
        lst.insert(rand, 99)
    return lst


def deque_append(deq):
    for i in range(100):
        deq.append(99)
    return deq


def deque_append_left(deq):
    for i in range(100):
        deq.appendleft(99)
    return deq


def deque_insert_random(deq):
    for i in range(100):
        rand = randint(0, 100)
        deq.insert(rand, 99)
    return deq


def get_random_list(lst):
    for i in range(100):
        rand = randint(0, 100)
        n = lst[rand]


def get_random_deque(deq):
    for i in range(100):
        rand = randint(0, 100)
        n = deq[rand]


my_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_deque = deque(my_list)

print(f"Добавление в конец списка: "
      f"{timeit('list_append(my_list)', 'from __main__ import list_append, my_list', number=1000)}")
print(f"Добавление в конец дека: "
      f"{timeit('deque_append(my_deque)', 'from __main__ import deque_append, my_deque', number=1000)}")
print(f"Добавление в начало списка: "
      f"{timeit('list_insert_left(my_list)', 'from __main__ import list_insert_left, my_list', number=1000)}")
print(f"Добавление в начало дека: "
      f"{timeit('deque_append_left(my_deque)', 'from __main__ import deque_append_left, my_deque', number=1000)}")
print(f"Добавление в случайное место списка: "
      f"{timeit('list_insert_random(my_list)', 'from __main__ import list_insert_random, my_list', number=1000)}")
print(f"Добавление в случайное место дека: "
      f"{timeit('deque_insert_random(my_deque)', 'from __main__ import deque_insert_random, my_deque', number=1000)}")
print(f"Получение случайного элемента из списка: "
      f"{timeit('get_random_list(my_list)', 'from __main__ import get_random_list, my_list', number=1000)}")
print(f"Получение случайного элемента из дека: "
      f"{timeit('get_random_deque(my_deque)', 'from __main__ import get_random_deque, my_deque', number=1000)}")

"""
Выаод:
    Время добавления элементов в конец списка и дека происходит примерно одинаково.
    Добавление элементов в начало или в случайное место дека происходит гораздно быстрее, чем в начало списка.
    Время получения элементов из списка и из дека примерно одинаково.
"""
