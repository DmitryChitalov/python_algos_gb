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


def u_list(u_list):
    user_deque = u_list
    user_deque.append(9)
    user_deque.pop()
    user_deque.extend(user_deque)
    user_deque = deque(u_list)
    user_deque.remove(1)
    user_deque = deque(u_list)
    user_deque.reverse()
    user_deque = deque(u_list)
    user_deque.rotate(3)
    return


def deq(u_list):
    user_deque = deque(u_list)
    user_deque.append(9)
    user_deque.pop()
    user_deque.extend(user_deque)
    user_deque = deque(u_list)
    user_deque.remove(1)
    user_deque = deque(u_list)
    user_deque.reverse()
    user_deque = deque(u_list)
    user_deque.rotate(3)
    return


print(f'скорость выполнения deque:',
      round(timeit.timeit("deq([1,2,3,4,5])", setup="from __main__ import deq", number=100000), 4))
print(f'скорость выполнения list:',
      round(timeit.timeit("u_list([1,2,3,4,5])", setup="from __main__ import u_list", number=100000), 4))

"""
Задача 3.
на выбранных операциях list оказался быстрее, но deque  содержит ряд функций отсутствующих в list
"""
