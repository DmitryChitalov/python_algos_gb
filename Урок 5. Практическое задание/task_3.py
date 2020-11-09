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

range_list = [el for el in range(1000)]
range_deque = deque(range_list)
num = 1000

#добавление в конец

def list_append(num):
    test_list = []
    for i in range(num):
        test_list.append(i)

def deque_append(num):
    test_deque = deque()
    for i in range(num):
        test_deque.append(i)

print(f'Добавление в список {num} элементов - {timeit.timeit("list_append(num)", setup="from __main__ import list_append, num", number=1000)}')
print(f'Добавление в deque {num} элементов - {timeit.timeit("deque_append(num)", setup="from __main__ import deque_append, num", number=1000)}')

# добавление слева


def list_appendleft(num):
    test_list = []
    for i in range(num):
        test_list.insert(0, i)

def deque_appendleft(num):
    test_deque = deque()
    for i in range(num):
        test_deque.appendleft(i)

print(f'Добавление в список слева {num} элементов - {timeit.timeit("list_appendleft(num)", setup="from __main__ import list_appendleft, num", number=1000)}')
print(f'Добавление в deque слева {num} элементов - {timeit.timeit("deque_appendleft(num)", setup="from __main__ import deque_appendleft, num", number=1000)}')

# расширение

def list_extend(range_list):
    test_list = []
    test_list.extend(range_list)

def deque_extend(range_deque):
    test_deque = deque()
    test_deque.extend(range_deque)

print(f'Расширение списка - {timeit.timeit("list_extend(range_list)", setup="from __main__ import list_extend, range_list", number=1000)}')
print(f'Расширение deque - {timeit.timeit("deque_extend(range_deque)", setup="from __main__ import deque_extend, range_deque", number=1000)}')

# расширение слева

def list_extendleft(range_list):
    test_list = []
    for el in range_list:
        test_list.insert(0, el)

def deque_extendleft(range_deque):
    test_deque = deque()
    test_deque.extendleft(range_deque)

print(f'Расширение списка слева - {timeit.timeit("list_extendleft(range_list)", setup="from __main__ import list_extendleft, range_list", number=1000)}')
print(f'Расширение deque слева - {timeit.timeit("deque_extendleft(range_deque)", setup="from __main__ import deque_extendleft, range_deque", number=1000)}')

# удаление элементов с конца

def list_pop(range_list):
    for i in range(len(range_list)):
        el = range_list.pop()

def deque_pop(range_deque):
    for i in range(len(range_deque)):
        el = range_deque.pop()

print(f'Удаление элементов списка с конца - {timeit.timeit("list_pop(range_list)", setup="from __main__ import list_pop, range_list", number=1000)}')
print(f'Удаление элементов deque с конца- {timeit.timeit("deque_pop(range_deque)", setup="from __main__ import deque_pop, range_deque", number=1000)}')

#удаление слева

def list_popleft(range_list):
    for i in range(len(range_list)):
        el = range_list.pop(0)

def deque_popleft(range_deque):
    for i in range(len(range_deque)):
        el = range_deque.popleft()

print(f'Удаление элементов списка слева - {timeit.timeit("list_popleft(range_list)", setup="from __main__ import list_popleft, range_list", number=1000)}')
print(f'Удаление элементов deque слева - {timeit.timeit("deque_popleft(range_deque)", setup="from __main__ import deque_popleft, range_deque", number=1000)}')

"""
Замеры показывают что deque работает быстрее на операциях добавления 
в список и расшрения и удаления элемнтов слева
"""