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


"""
Не оптимизированная функция recursive_reverse
0.029160999999999992
0.032773699999999906
0.05883189999999994
Оптимизированная функция recursive_reverse_mem
0.0020951999999999638
0.001666999999999974
0.0017553999999999625
"""

# Как вариант, можем упростить мемоизацию:


def memoize_2(f):
    def wrapper(n, cache={}):
        r = cache.get(n)
        if r is None:
            r = f(n)
            cache[n] = r
        return r
    return wrapper


@memoize_2
def recursive_reverse_mem_2(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem_2')
print(
    timeit(
        'recursive_reverse_mem_2(num_100)',
        setup='from __main__ import recursive_reverse_mem_2, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_2(num_1000)',
        setup='from __main__ import recursive_reverse_mem_2, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_2(num_10000)',
        setup='from __main__ import recursive_reverse_mem_2, num_10000',
        number=10000))


"""
Не оптимизированная функция recursive_reverse
0.028271600000000004
0.0346103
0.059271500000000005
Оптимизированная функция recursive_reverse_mem
0.002665700000000021
0.002874200000000021
0.0028074000000000154
Оптимизированная функция recursive_reverse_mem_2
0.0020699000000000134
0.001511200000000018
0.0020651999999999893
"""