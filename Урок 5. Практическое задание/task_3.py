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
import string
import time
import timeit
from collections import deque


def my_timer(f):
    def tmp(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        delta_time = time.time() - start_time
        print('Время выполнения функции {}'.format(delta_time))
        return result

    return tmp


def create_list():
    return [c * 3 for c in range(100)]


def deque_rotate():
    global new_deque
    for i in range(100):
        new_deque = deque(string.ascii_uppercase)
    return new_deque


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if int(nums[i]) % 2 == 0]
    return new_arr


if __name__ == '__main__':
    nums = "1234567890"

    print(timeit.timeit("create_list()", setup="from __main__ import create_list", number=1000))
    print(timeit.timeit("deque_rotate()", setup="from __main__ import deque_rotate", number=1000))