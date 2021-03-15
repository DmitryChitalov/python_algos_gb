from memory_profiler import profile

from timeit import timeit
from random import randint


@profile
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@profile
def f_reverse(number, reverse_str=''):
    len_str = len(str(number))
    if len_str == 0:
        return reverse_str
    else:
        reverse_str += number[-1]
        len_str -= 1
        return f_reverse(number[:-1], reverse_str)


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@profile
@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


num_100 = 100
num_1000 = 1000
num_10000 = 10000

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10))

print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10))

n_100 = str(num_100)
n_1000 = str(num_1000)
n_10000 = str(num_10000)

print('f_reverse')
print(
    timeit(
        "f_reverse(n_100)",
        setup='from __main__ import f_reverse, n_100',
        number=10))

print(
    timeit(
        "f_reverse(n_1000)",
        setup='from __main__ import f_reverse, n_1000',
        number=10))

print(
    timeit(
        "f_reverse(n_10000)",
        setup='from __main__ import f_reverse, n_10000',
        number=10))

"""
Решение с использованием мемоизации получилось незначительно, но самым экономичным по памяти.

Не оптимизированная функция recursive_reverse
Filename: C:/Python/GeekBrain/python_algos_gb_DP/lesson_6/task_1_2.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     9     32.9 MiB     32.9 MiB           1   @profile
    10                                         def recursive_reverse(number):
    11     32.9 MiB      0.0 MiB           1       if number == 0:
    12     32.9 MiB      0.0 MiB           1           return str(number % 10)
    13                                             return f'{str(number % 10)}{recursive_reverse(number // 10)}'


оптимизированная функция recursive_reverse_mem
Filename: C:/Python/GeekBrain/python_algos_gb_DP/lesson_6/task_1_2.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     32.8 MiB     32.8 MiB           1       def decorate(*args):
    30                                         
    31     32.8 MiB      0.0 MiB           1           if args in cache:
    32                                                     return cache[args]
    33                                                 else:
    34     32.8 MiB      0.0 MiB           1               cache[args] = f(*args)
    35     32.8 MiB      0.0 MiB           1               return cache[args]


оптимизированная функция recursive_reverse_mem
Filename: C:/Python/GeekBrain/python_algos_gb_DP/lesson_6/task_1_2.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     33.4 MiB     33.4 MiB           1       def decorate(*args):
    29                                         
    30     33.4 MiB      0.0 MiB           1           if args in cache:
    31                                                     return cache[args]
    32                                                 else:
    33     33.4 MiB      0.0 MiB           1               cache[args] = f(*args)
    34     33.4 MiB      0.0 MiB           1               return cache[args]

"""


