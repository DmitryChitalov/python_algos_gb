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
"""В данной задаче предложил 2 решения: через .join и slice
В итоге на первом месте (самое быстрое решение) recursive_reverse_mem   (0.0021)
на втором reverse_by_slice   (0,0046) в два раза медленнее
на третьем reverse_by_join  (0,016) примерно в 7.5 раз медленнее
на последнем recursive_reverse (0,035) примерно в 16,5 раз медленнее

Получается, что решение через мемоизацию самое оптимальное, и даже join со сложносью O(1) и
slice - O(1) проигрывают ему.
Вывод: на данной задаче стоит применять slice - реверс на месте, или рекурсию с мемоизацией."""

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


def reverse_by_join(number):
    reversed_number = [''.join(i for i in str(number)[::-1])]
    return reversed_number


print('Функция reverse_by_join')
print(
    timeit(
        "reverse_by_join(num_100)",
        setup='from __main__ import reverse_by_join, num_100',
        number=10000))
print(
    timeit(
        "reverse_by_join(num_1000)",
        setup='from __main__ import reverse_by_join, num_1000',
        number=10000))
print(
    timeit(
        "reverse_by_join(num_10000)",
        setup='from __main__ import reverse_by_join, num_10000',
        number=10000))


def reverse_by_slice(number):
    reversed_number = str(number)[::-1]
    return reversed_number


print('Функция reverse_by_slice')
print(
    timeit(
        "reverse_by_slice(num_100)",
        setup='from __main__ import reverse_by_slice, num_100',
        number=10000))
print(
    timeit(
        "reverse_by_slice(num_1000)",
        setup='from __main__ import reverse_by_slice, num_1000',
        number=10000))
print(
    timeit(
        "reverse_by_slice(num_10000)",
        setup='from __main__ import reverse_by_slice, num_10000',
        number=10000))
