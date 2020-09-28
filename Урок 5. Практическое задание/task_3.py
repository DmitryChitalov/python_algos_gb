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
import time
from collections import deque

my_list = [2, 11, 44, 55, 47, 89, 41, 47, 98, 102]
my_deque = deque(my_list)
print(my_deque)


def append_my_list(lst, el):
    return lst.append(el)


def append_my_deque(dq, el):
    return dq.append(el)


def pop_my_list(lst):
    return lst.pop(0)


def pop_my_deque(dq):
    return dq.popleft()


def access_to_item(lst):
    return lst[4:]


def access_to_item_dq(dq):
    return dq[4:]


print('Вставка элемента в список')  # 8.369999999999905e-05
print(timeit('lambda: append_my_list(my_list, 10)', setup='from __main__ import append_my_list', number=1000))
print('Вставка элемента в deque')  # 5.6500000000000994e-05
print(timeit('lambda: append_my_list(my_deque, 10)', setup='from __main__ import append_my_deque', number=1000))
# метод вставки в deque заметно быстрее
print('Удаление элемента из списка')  # 8.309999999999915e-05
print(pop_my_list(my_list))
print(timeit('lambda: pop_my_list(my_list)', setup='from __main__ import pop_my_list', number=1000))
print('Удаление элемента из deque')  # 8.260000000000212e-05
print(timeit('lambda: pop_my_deque(my_deque)', setup='from __main__ import pop_my_deque', number=1000))
print('срезы в списке')  # 8.450000000000124e-05
print(timeit('lambda: access_to_item(my_list)', setup='from __main__ import access_to_item', number=1000))
print('срезы в deque')   # 8.279999999999399e-05
print(timeit('lambda: access_to_item_dq(my_deque)', setup='from __main__ import access_to_item_dq', number=1000))
# из показанных результатов видно, что информация соответствует действительности
