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

import random
from timeit import timeit

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


low_number = randint(1, 10000)
biger_number = randint (10000, 1000000)

print(timeit("recursive_reverse(low_number)",
             setup='from __main__ import recursive_reverse, low_number',
             number=10000))

print(timeit("recursive_reverse(biger_number)",
             setup='from __main__ import recursive_reverse, biger_number',
             number=10000))


def memoize(function):
    memory = {}

    def decorator(*args):
        if args in memory:
            return memory[args]
        else:
            memory[args] = function(*args)
            return memory[args]
    return decorator

@memoize
def recursive_reverse_momoized(number):
    if number ==0:
        return ""
    return f'{str(number % 10)}{recursive_reverse_momoized(number // 10)}'

