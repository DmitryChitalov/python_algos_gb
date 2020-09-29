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
from random import randint
import cProfile

s_list = [randint(0, 2000) for _ in range(100)]
s_deq = deque([randint(0, 2000) for _ in range(100)])


def list_speed_test():
    s_list.append(2)
    s_list.insert(5, 1)
    s_list.pop(5)
    s_list.pop()


def deque_speed_test():
    s_deq.appendleft(1)
    s_deq.append(1)
    s_deq.popleft()
    s_deq.pop()


print(timeit('list_speed_test()', setup='from __main__ import list_speed_test'))
print(timeit('deque_speed_test()', setup='from __main__ import deque_speed_test'))

print(cProfile.run('''def list_speed_test():
    s_list.append(2)
    s_list.insert(5, 1)
    s_list.pop(5)
    s_list.pop()'''))


print(cProfile.run('''def deque_speed_test():
    s_deq.appendleft(1)
    s_deq.append(1)
    s_deq.popleft()
    s_deq.pop()'''))


# операции с очередью быстрее и эффективнее по времени
