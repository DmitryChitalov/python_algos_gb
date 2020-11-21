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
from random import randint

list_1 = [randint(1, 1000) for _ in range(50)]
deque_1 = deque(list_1)
randoms_array = [randint(0, 49) for _ in range(5)]


def print_list():
    for i in list_1:
        print(i, end=' ')


def print_deque():
    for i in deque_1:
        print(i, end=' ')


# def list_append():
#     for i in range(5):
#         list_1.append(randint(1, 100))
#
#
# def deque_append():
#     for _ in range(5):
#         deque_1.append(randint(1, 100))


def deque_append_left():
    deque_1.appendleft(randint(1, 100))


def list_insert_left():
    list_1.insert(randoms_array[1], randint(1, 100))


# def deque_insert():
#     for i in range(5):
#         deque_1.insert(randoms_array[i], randint(1, 100))


def list_rotate_x5():
    for _ in range(5):
        list_1[0], list_1[-1] = list_1[-1], list_1[0]


def deque_rotate_x5():
    deque_1.rotate(5)


def random_list_access():
    a = list_1[randint(0, 49)]


def random_deque_access():
    b = deque_1[randint(0, 49)]


print(f'\n\n'
      f'Вывод элементов из списка:\n'
      f'{timeit("print_deque()", setup="from __main__ import print_deque", number=10000)} секунд;\n'
      f'Вывод элементов из дека:\n'
      f'{timeit("print_list()", setup="from __main__ import print_list", number=10000)} секунд;\n'
      f'Добавление элемента в начало дека:\n'
      f'{timeit("deque_append_left()", setup="from __main__ import deque_append_left", number=10000)} секунд;\n'
      f'Вставка элемента в начало списка:\n'
      f'{timeit("list_insert_left()", setup="from __main__ import list_insert_left", number=10000)} секунд;\n'
      f'"Поворот" списка (5 раз, с конца в начало):\n'
      f'{timeit("list_rotate_x5()", setup="from __main__ import list_rotate_x5", number=10000)} секунд;\n'
      f'"Поворот" дека (5 раз, с конца в начало):\n'
      f'{timeit("deque_rotate_x5()", setup="from __main__ import deque_rotate_x5", number=10000)} секунд;\n'
      f'Доступ к случайному элементу в списке:\n'
      f'{timeit("random_list_access()", setup="from __main__ import random_list_access", number=10000)} секунд;\n'
      f'Доступ к случайному элементу в деке:\n'
      f'{timeit("random_deque_access()", setup="from __main__ import random_deque_access", number=10000)} секунд.\n')

'''
Вывод: информация в документации полностью соответствует действительности.
Добавление элементов в дек происходит в несколько раз быстрее, чем в список, 
в то время как доступ к случайному элементу со списком работает быстрее, чем с деком.
'''
