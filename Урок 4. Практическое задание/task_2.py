"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
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

def slice_method(nums):
    new_str = str(nums)[::-1]
    return new_str


print('Функция с использованием среза')
print(
    timeit(
        'slice_method(num_100)',
        setup='from __main__ import slice_method, num_100',
        number=10000))
print(
    timeit(
        'slice_method(num_1000)',
        setup='from __main__ import slice_method, num_1000',
        number=10000))
print(
    timeit(
        'slice_method(num_10000)',
        setup='from __main__ import slice_method, num_10000',
        number=10000))


def cycle_method(nums):
    new_str = ''
    for el in str(nums):
        new_str = el + new_str
    return new_str

print('Функция с использованием цикла')
print(
    timeit(
        'cycle_method(num_100)',
        setup='from __main__ import cycle_method, num_100',
        number=10000))
print(
    timeit(
        'cycle_method(num_1000)',
        setup='from __main__ import cycle_method, num_1000',
        number=10000))
print(
    timeit(
        'cycle_method(num_10000)',
        setup='from __main__ import cycle_method, num_10000',
        number=10000))

"""

    Альтернативные варианты решения с помошью среза и цикла не улучшили время выполнения кода.
    Сложность функции с использованием срезов константная О(1)
    Сложность функции с использованием циклов линейная О(n)
    Решение с использованием декоратора показывает наилучший резултрат по вермени выполнения.

Не оптимизированная функция recursive_reverse
0.02700720000000001
0.031185500000000005
0.05440050000000002
Оптимизированная функция recursive_reverse_mem
0.0020171999999999968
0.001968400000000009
0.002030099999999979
Функция с использованием срезов
0.0040141999999999955
0.0040797999999999945
0.003983300000000023
Функция с использованием цикла
0.007694100000000009
0.00870689999999999
0.013052399999999992


"""
