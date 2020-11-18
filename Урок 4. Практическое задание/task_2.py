"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию
"""

from timeit import timeit
from random import randint


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate

def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

@memoize
def recursive_reverse_2(numb):
    if numb == 0:
        return ''
    return f'{str(numb % 10)}{recursive_reverse_2(numb // 10)}'


nums = randint(10000, 1000000)

print(f'{recursive_reverse(nums)}')
print(f'{recursive_reverse_2(nums)}')
print('До оптимизации:\n')
print(
    timeit(
        "recursive_reverse(nums)",
        setup='from __main__ import recursive_reverse, nums',
        number=100000
    ))

print('После оптимизации:\n')
print(
    timeit(
        'recursive_reverse_2(nums)',
        setup='from __main__ import recursive_reverse_2, nums',
        number=100000
    ))

# Благодаря введению памяти скорость обработки задачи изменилась с 0,5 до 0,04 сек
