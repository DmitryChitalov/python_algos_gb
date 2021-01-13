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
import timeit

test_time_list = """
a = [n for n in range(100000)]
i = 0
while i < 1000:
    a.insert(0, i)
    i += 1
"""

test_time_deque = """
from collections import deque
b = [n for n in range(100000)]
deq_obj = deque(b)
k = 0
while k < 1000:
    deq_obj.appendleft(k)
    k += 1
"""

elapsed_time_list = timeit.timeit(test_time_list, number=100)
print(f"Время list {elapsed_time_list}")
elapsed_time_deque = timeit.timeit(test_time_deque, number=100)
print(f"Время deque {elapsed_time_deque}")

# deque очевидно быстрее работает чем list
