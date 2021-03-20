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

def append_left_list(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def append_left_deque(num):
    my_deque = deque()
    for i in range(num):
        my_deque.appendleft(i)

num = 1000

my_list1 = [el for el in range(num)]
my_deque1 = deque(my_list1)

print(f"append_left_list({num}): ",
      timeit(f"append_left_list({num})", globals=globals(), number=1000))
print(f"append_left_deque({num}): ",
      timeit(f"append_left_deque({num})", globals=globals(), number=1000))
