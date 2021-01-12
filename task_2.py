"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(10000000, 10000000000000)
print(num_100)
print(num_1000)
print(num_10000)

print(timeit("recursive_reverse(num_100)",
             setup="from __main__ import recursive_reverse, num_100",
             number=10000))
print(timeit("recursive_reverse(num_1000)",
             setup="from __main__ import recursive_reverse, num_1000",
             number=10000))
print(timeit("recursive_reverse(num_10000)",
             setup="from __main__ import recursive_reverse, num_10000",
             number=10000))


def memoize(f):
    cach = {}
    def decorate(*args):
        if args in cach:
            return cach[args]
        else:
            cach[args] = f(*args)
            return cach[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print(timeit("recursive_reverse_mem(num_100)",
             setup="from __main__ import recursive_reverse_mem, num_100",
             number=10000))
print(timeit("recursive_reverse_mem(num_1000)",
             setup="from __main__ import recursive_reverse_mem, num_1000",
             number=10000))
print(timeit("recursive_reverse_mem(num_10000)",
             setup="from __main__ import recursive_reverse_mem, num_10000",
             number=10000))
"""
0.056351
0.06229409999999999
0.11715119999999998
0.00488050000000001
0.004960099999999967
0.004966999999999999

Первые три замера показывают значительно большее время при любой длинне числа.
Делаем вывод - мемоизация нужна.
"""
