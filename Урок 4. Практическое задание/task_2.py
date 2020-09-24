"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        # return str(number % 10)
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

"""
Не оптимизированная функция recursive_reverse
0.0503561
0.037659399999999996
0.07746900000000001
Оптимизированная функция recursive_reverse_mem
0.002310500000000021
0.0023405999999999982
0.0022517999999999982
Оптимизированная функция my_reverse
0.00433550000000002
0.00433710000000001
0.004726800000000003

По результатам замеров можно однозначно сказать:
Вариант рекурсии с мемоизацией выигрывает у просто рекурсии.

Попытка оптимизации через срез строки.
Моя оптимизация показала отличный результат относительно рекурсии,
но проиграла рекурсии с мемоизацией.
"""


def my_reverse(number):
    s = str(number)
    return s[::-1]


print('Оптимизированная функция my_reverse')
print(
    timeit(
        'my_reverse(num_100)',
        setup='from __main__ import my_reverse, num_100',
        number=10000))
print(
    timeit(
        'my_reverse(num_1000)',
        setup='from __main__ import my_reverse, num_1000',
        number=10000))
print(
    timeit(
        'my_reverse(num_10000)',
        setup='from __main__ import my_reverse, num_10000',
        number=10000))
