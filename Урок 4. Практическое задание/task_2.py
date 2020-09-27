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

print('Неоптимизированная функция recursive_reverse')
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


# вариант оптимизации без memoize

print('Предлагаемый вариант дополнительной оптимизации функции reverse_num_optimized')


def reverse_num_optimized(number):
    num = number
    num = int(str(num)[::-1])
    return f'{num}'


print(
    timeit(
        'reverse_num_optimized(num_100)',
        setup='from __main__ import reverse_num_optimized, num_100',
        number=10000))
print(
    timeit(
        'reverse_num_optimized(num_1000)',
        setup='from __main__ import reverse_num_optimized, num_1000',
        number=10000))
print(
    timeit(
        'reverse_num_optimized(num_10000)',
        setup='from __main__ import reverse_num_optimized, num_10000',
        number=10000))

# вариант оптимизации c memoize
print('Предлагаемый вариант оптимизации функции reverse_num_optimized с memoize')


def memoize2(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize2
def reverse_num_optimized_meme(number):
    num = number
    num = int(str(num)[::-1])
    return f'{num}'


print(
    timeit(
        'reverse_num_optimized_meme(num_100)',
        setup='from __main__ import reverse_num_optimized_meme, num_100',
        number=10000))
print(
    timeit(
        'reverse_num_optimized_meme(num_1000)',
        setup='from __main__ import reverse_num_optimized_meme, num_1000',
        number=10000))
print(
    timeit(
        'reverse_num_optimized_meme(num_10000)',
        setup='from __main__ import reverse_num_optimized_meme, num_10000',
        number=10000))

'''
Неоптимизированная функция recursive_reverse
0.06428199999999999
0.054964700000000005
0.08070019999999999
Оптимизированная функция recursive_reverse_mem
0.0035169999999999924
0.003278200000000009
0.004054200000000008
Предлагаемый вариант дополнительной оптимизации функции (reverse_num_optimized) без memoize
0.009247399999999989
0.006985599999999981
0.007978700000000005
Предлагаемый вариант дополнительной оптимизации функции (reverse_num_optimized_meme) с memoize
0.0019560000000000133
0.0025261999999999785
0.0022312999999999916

Очевидно,что мемоизация значительно повышает скорость выполнения функции в обоих вариантах.
Основная причина повышения эффективности - многократное повторное использование результатов работы функции по
расчету числа, обратного введенному. 
'''
