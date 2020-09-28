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

# Меморизация дает существенный выигрыш по производительности
# при многократном вызове функции с одним и тем же аргиментом
# т.к. сокращает количество рекурсивных вызовов.
# При однократном выполнении выигрыша не будет.
#
# Для оптимизации использовал штатный механизм python для работы со строкой + меморизацию
# из functools. Меморизация опять же имеет смысл при многократном выполнении функции с 1 и тем же
# аргументом.

from timeit import timeit
from random import randint
from functools import lru_cache


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

rep = 100000

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=rep))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=rep))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=rep))


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
        number=rep))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=rep))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=rep))


@lru_cache
def reverse_slice(number):
    return str(number)[::-1]


print('Функция, реализованная с помощью среза.')
print(
    timeit(
        'reverse_slice(num_100)',
        setup='from __main__ import reverse_slice, num_100',
        number=rep))
print(
    timeit(
        'reverse_slice(num_1000)',
        setup='from __main__ import reverse_slice, num_1000',
        number=rep))
print(
    timeit(
        'reverse_slice(num_10000)',
        setup='from __main__ import reverse_slice, num_10000',
        number=rep))
