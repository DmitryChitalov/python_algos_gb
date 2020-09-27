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
########################################################################################################################

from collections import deque
from timeit import timeit

some_list = [i for i in range(100)]
some_deque = deque(some_list)


def list_index_add_pop(arr):
    arr.insert(0, 0)
    arr.pop(0)
    arr.append(10)
    arr.pop()


print(
    timeit(
        'list_index_add_pop(some_list)',
        setup='from __main__ import list_index_add_pop, some_list',
        number=1000
    )
)


def deque_index_add_pop(arr):
    arr.appendleft(0)
    arr.append(10)
    arr.popleft()
    arr.pop()


print(
    timeit(
        'deque_index_add_pop(some_deque)',
        setup='from __main__ import deque_index_add_pop, some_deque',
        number=1000
    )
)


"""
        Благодаря дополнительным функциям, deque выполняет вставку и извлечение
     из начала списка в два раза быстрее обычного массива. 

"""
