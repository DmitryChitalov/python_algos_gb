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

my_list = list()
my_deque = deque()


def list_append():
    for i in range(1000):
        my_list.append(i)


def deque_append():
    for i in range(1000):
        my_deque.append(i)


print("Добавление элементов в конец")
print(timeit("list_append()", "from __main__ import list_append", number=1000))
print(timeit("deque_append()", "from __main__ import deque_append", number=1000))


def list_insert():
    """list.insert(0, i) == deque.appendleft(i)"""
    my_list.insert(0, 100)


def deque_appendleft():
    my_deque.appendleft(100)


print("Добавление элементов в начало")
print(timeit("list_insert()", "from __main__ import list_insert", number=1000))
print(timeit("deque_appendleft()", "from __main__ import deque_appendleft", number=1000))


def list_pop():
    return my_list.pop()


def deque_pop():
    return my_deque.pop()


print("Извлечение последнего элемента")
print(timeit("list_pop()", "from __main__ import list_pop", number=1000))
print(timeit("deque_pop()", "from __main__ import deque_pop", number=1000))


def list_pop_left():
    return my_list.pop(0)


def deque_pop_left():
    return my_deque.popleft()


print("Извлечение первого элемента")
print(timeit("list_pop_left()", "from __main__ import list_pop_left", number=1000))
print(timeit("deque_pop_left()", "from __main__ import deque_pop_left", number=1000))


def list_get():
    return my_list[0]


def deque_get():
    return my_deque[0]


print("Извлечение элемента по индексу")
print(timeit("list_get()", "from __main__ import list_get", number=10000000))
print(timeit("deque_get()", "from __main__ import deque_get", number=10000000))


"""
Добавление элементов в конец:
list - 0.0984158
deque - 0.0837424

Добавление элементов в начало:
list - 0.6703925
deque - 0.00012900000000004574

Извлечение последнего элемента:
list - 0.00016839999999995747
deque - 0.00012690000000004087

Извлечение первого элемента:
list - 0.26226459999999996
deque - 0.0001238999999999546

Извлечение элемента по индексу:
list - 0.8857516000000003
deque - 0.9696625000000001

Deque превосходит по скорости добавлению и извлечению.
Однако операции с получением по индексу list выполняет чуть быстрее
"""