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

from random import randint
from timeit import timeit


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
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


@memoize
def recursive_reverse_mem1(number):
    if number == 0:
        return ''
    return f'{number % 10}{recursive_reverse_mem1(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem1')
print(
    timeit(
        'recursive_reverse_mem1(num_100)',
        setup='from __main__ import recursive_reverse_mem1, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem1(num_1000)',
        setup='from __main__ import recursive_reverse_mem1, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem1(num_10000)',
        setup='from __main__ import recursive_reverse_mem1, num_10000',
        number=10000))

"""
1. мемоизация нужна, т.к. сильно сокращает время выполнения программы:
Не оптимизированная функция recursive_reverse
0.033445538
0.038533392
0.06844129999999998
Оптимизированная функция recursive_reverse_mem
0.002385067000000074
0.002456581999999985
0.002490007999999988

2. возможная оптимизация - избавиться от приведения результата от деления с остатком к строке, 
т.к. ф-я f и так приводит число к строке, но выигрыш по времени не такой большой и критичный
Не оптимизированная функция recursive_reverse
0.03342932500000001
0.03864495400000001
0.068731559
Оптимизированная функция recursive_reverse_mem
0.0026628419999999986
0.0029004639999999915
0.0028723910000000297
Оптимизированная функция recursive_reverse_mem1
0.002658086000000004
0.0025557179999999846
0.0025375620000000487
"""
