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
def rotate_with_list(items=range(100000), n=800):
    l = list(items)
    for _ in range(n):
        l.append(l.pop(0))
    return l

from collections import deque
def rotate_with_deque(items=range(100000), n=800):
    d = deque(items)
    for _ in range(n):
        d.append(d.popleft())
    return d

print(timeit('rotate_with_list(items=range(100000), n=800)', setup='from __main__ import rotate_with_list', number=1000))
print(timeit('rotate_with_deque(items=range(100000), n=800)', setup='from __main__ import rotate_with_deque', number=1000))

'''
9.7296462 - время списка
2.5429788 - время deque
'''