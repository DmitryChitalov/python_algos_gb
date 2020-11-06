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


def deq_check(lst):
    deq_obj = deque(lst)
    deq_obj.append('123')
    deq_obj.appendleft('456')
    deq_obj.rotate(1)
    deq_obj.popleft()
    deq_obj.extend(list(range(10, 150)))
    for el in deq_obj:
        el += el


def list_check(lst):
    list_obj = list(lst)
    list_obj.append('123')
    list_obj.insert(0, '456')
    list_obj.insert(0, list_obj[len(list_obj) - 1])
    list_obj.pop()
    list_obj.pop(0)
    list_obj.extend(list(range(10, 150)))
    for el in list_obj:
        el += el


string = 'dfv dsfvfd dfvdfv'
print(timeit.timeit(f'deq_check({string.split()})', setup="from __main__ import deq_check", number=10000))
print(timeit.timeit(f'list_check({string.split()})', setup="from __main__ import list_check", number=10000))

"""
Очередь быстрее в функциях appendleft, extend, popleft
На маленьких объемах данных разницы между списком и очередью по поизводительности нет.
"""
