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


def f_reverse(number, reverse_str=''):
    len_str = len(str(number))
    if len_str == 0:
        return reverse_str
    else:
        reverse_str += number[-1]
        len_str -= 1
        return f_reverse(number[:-1], reverse_str)


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

n_100 = str(num_100)
n_1000 = str(num_1000)
n_10000 = str(num_10000)

print('f_reverse')
print(
    timeit(
        "f_reverse(n_100)",
        setup='from __main__ import f_reverse, n_100',
        number=10000))

print(
    timeit(
        "f_reverse(n_1000)",
        setup='from __main__ import f_reverse, n_1000',
        number=10000))

print(
    timeit(
        "f_reverse(n_10000)",
        setup='from __main__ import f_reverse, n_10000',
        number=10000))

"""
решение через мемоизацию работает в 20 раз быстрее!!!

Оптимизация не получилась. Решение через функцию получилось самым медленным
"""
