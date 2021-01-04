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


def reverse(n):
    return int(''.join(reversed(str(n))))


@memoize
def reverse_mem(n):
    return int(''.join(reversed(str(n))))


def reverse_1(n):
    r_n = str(n)[::-1]
    return int(r_n)


@memoize
def reverse_1_mem(n):
    r_n = str(n)[::-1]
    return int(r_n)


num_10000 = randint(100000000, 10000000000000)
print('Функция reverse')
print(
    timeit(
        'reverse(num_10000)',
        setup='from __main__ import reverse, num_10000',
        number=10000))
num_10000 = randint(100000000, 10000000000000)
print('Функция reverse_mem')
print(
    timeit(
        'reverse_mem(num_10000)',
        setup='from __main__ import reverse_mem, num_10000',
        number=10000))
num_10000 = randint(100000000, 10000000000000)
print('Функция reverse_1')
print(
    timeit(
        'reverse_1(num_10000)',
        setup='from __main__ import reverse_1, num_10000',
        number=10000))
num_10000 = randint(100000000, 10000000000000)
print('Функция reverse_1_mem')
print(
    timeit(
        'reverse_1_mem(num_10000)',
        setup='from __main__ import reverse_1_mem, num_10000',
        number=10000))

"""
Как мы видим из замеров мемоизация значительно увеличивает скорость выполнения как функции написанной 
при помощи рекурсии, так и обычной функции.
Однако если обычные функции без мемоизации значительно выигрывают по скорости у функций с рекурсией без мемоизации, 
то в функциях с мемоизацией скорость выполнения различается на десятитысячные доли.

Мемоизация нужна, посколько скорость выполнения с ее использованием значительно превосходит скорость выполнения без.
"""
