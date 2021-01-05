"""
Задача 3.
В соответствии с документацией Python, deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации соответствует дейстивтельности.
"""
from collections import deque
from timeit import timeit


def deque_append_left():
    for i in range(10):
        deq.appendleft(i)
    return


def list_insert():
    for i in range(10):
        lst.insert(0, i)
    return


def deque_pop_left():
    return deq.popleft()


def list_pop():
    return lst.pop(0)


def deque_get():
    for i in range(100):
        deq[i]
    return


def list_get():
    for i in range(100):
        lst[i]
    return


lst = [i for i in range(1000)]
deq = deque(lst)

print(timeit('deque_append_left()', 'from __main__ import deque_append_left', number=10000))  # 0.010695555000000002
print(timeit('list_insert()', 'from __main__ import list_insert', number=10000))  # 1.934272816

print(timeit('deque_pop_left()', 'from __main__ import deque_pop_left', number=10000))  # 0.00117518499999969
print(timeit('list_pop()', 'from __main__ import list_pop', number=10000))  # 0.2203707960000001

print(timeit('deque_get()', 'from __main__ import deque_get', number=10000))  # 0.039791123000000095
print(timeit('list_get()', 'from __main__ import list_get', number=10000))  # 0.033808421999999894


"""
По результатам замеров можно сделать вывод, что информация в документации соответствует дейстивтельности.
Добавление или извлечение начальных элементов на порядок происходит быстрее в deque, чем в list.
"""