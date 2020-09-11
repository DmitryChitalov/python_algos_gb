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
print(num_100)

print(timeit("recursive_reverse(num_100)",
             setup="from __main__ import recursive_reverse, num_100",
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

"""
Результаты замеров:
109645
0.051348399999999995
0.0040999999999999925
Вывод: мемоизация необходима так как значительно сокращает время работы кода.
"""