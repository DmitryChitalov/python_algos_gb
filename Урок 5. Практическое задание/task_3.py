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


def list_iter():
    for el in SOME_LIST:
        if el % 2 == 0:
            print(el, end=' ')
        else:
            continue
    return print()


def deque_iter():
    for el in SOME_DEQUE:
        if el % 2 == 0:
            print(el, end=' ')
        else:
            continue
    return print()


def list_append():
    for el in range(200, 1001, 2):
        SOME_LIST.append(el)
    return SOME_LIST


def deque_append():
    for el in range(200, 1001, 2):
        SOME_DEQUE.append(el)
    return SOME_DEQUE


def list_append_left():
    for el in range(200, 1001, 2):
        SOME_LIST.insert(0, el)
    return SOME_LIST              


def deque_append_left():
    for el in range(200, 1001, 2):
        SOME_DEQUE.appendleft(el)
    return SOME_DEQUE


def list_rotation(n):
    i = 0
    if n > 0:
        while i < n:
            SOME_LIST.insert(0, SOME_LIST.pop(len(SOME_LIST) - 1))
            i += 1
    elif n < 0:
        while i == abs(n):
            SOME_LIST.append(SOME_LIST.pop(0))
            i += 1
    else:
        return print(f'Вы ввели "0", ничего перемещать НЕ БУДУ!')
    return SOME_LIST


def deque_rotation(n):
    SOME_DEQUE.rotate(n)
    return SOME_DEQUE


SOME_LIST = [i for i in range(201)]
SOME_DEQUE = deque([i for i in range(201)])

print(f'-- List iter --')
print(timeit("list_iter()", setup="from __main__ import list_iter", number=1))
print(f'-- Deque iter--')
print(timeit("deque_iter()", setup="from __main__ import deque_iter", number=1))
print()


print(f'-- List append --')
print(timeit("list_append()", setup="from __main__ import list_append", number=100))
print(f'-- Deque append --')
print(timeit("deque_append()", setup="from __main__ import deque_append", number=100))
print()


print(f'-- List append-left --')
print(timeit("list_append_left()", setup="from __main__ import list_append_left", number=100))
print(f'-- Deque append-left --')
print(timeit("deque_append_left()", setup="from __main__ import deque_append_left", number=100))
print()


print(f'-- List rotation --')
print(timeit("list_rotation(2)", setup="from __main__ import list_rotation", number=1000))
print(f'-- Deque rotation --')
print(timeit("deque_rotation(2)", setup="from __main__ import deque_rotation", number=1000))
print()

"""
Утверждение в оф.документации верно! Стандартные операции выполняются можно сказать с одинаковой скоростью, а вот
не стандартые операции такие как например, добавить элемент слева, убрать с конца - добавить в начало, методами deque
выполняются на голову выше. И полученные замеры являются тому подтверждением.
"""


