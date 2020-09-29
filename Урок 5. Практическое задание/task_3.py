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

lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dq_1 = deque(lst_1)


def append_lst(lst, el):
    return lst.append(el)


def append_dq(dq, el):
    return dq.append(el)


def pop_lst(lst):
    return lst.pop(0)


def pop_dq(dq):
    return dq.popleft()


def get_lst(lst):
    return lst[3:]


def get_dq(dq):
    return dq[3:]


print(f'Вставка элемента в список занимает: '
      f'{timeit("lambda: append_lst(lst_1, 11)", setup="from __main__ import append_lst", number=1000)}')
print(f'Вставка элемента в список deque: '
      f'{timeit("lambda: append_dq(lst_1, 11)", setup="from __main__ import append_dq", number=1000)}')
print(f'Удаление элемента из списка занимает: '
      f'{timeit("lambda: pop_lst(lst_1, 11)", setup="from __main__ import pop_lst", number=1000)}')
print(f'Удаление элемента из deque занимает: '
      f'{timeit("lambda: pop_dq(lst_1, 11)", setup="from __main__ import pop_dq", number=1000)}')
print(f'Получение среза из списка занимает: '
      f'{timeit("lambda: get_lst(lst_1, 11)", setup="from __main__ import get_lst", number=1000)}')
print(f'Получение среза из deque занимает: '
      f'{timeit("lambda: get_dq(lst_1, 11)", setup="from __main__ import get_dq", number=1000)}')

# Вставка элемента в список занимает: 0.00013729999999999992
# Вставка элемента в список deque: 0.00013629999999999892
# Удаление элемента из списка занимает: 0.00013679999999999942
# Удаление элемента из deque занимает: 0.00013629999999999892
# Получение среза из списка занимает: 0.00013849999999999973
# Получение среза из deque занимает: 0.0001359000000000013
# Таким образом, действительно, операции с deque занимают меньше времени, чем со списком