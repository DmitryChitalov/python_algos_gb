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
Выводы: мемоизация здесь нужна, значительно сокращает время выполнения функции,
за счет того, что уменьшается количество вычислений за счет сохраненных значений
Не рекурсивное решение оказалось не лучше
Результаты измерений:

    Не оптимизированная функция recursive_reverse
        0.029354811
        0.029082107999999995
        0.052547257
        
    Оптимизированная функция recursive_reverse_mem
        0.0019488729999999899
        0.0019092049999999972
        0.001965313999999996
        
    Не рекурсивное решение:
        0.0030855720000000086
        0.0030146129999999993
        0.0031485229999999864
"""


def rev_num(num):
    return str(num)[::-1]


print ('Не рекурсивное решение:')
print (timeit(
            'rev_num(num_100)',
            setup='from __main__ import rev_num, num_100',
            number=10000))
print (timeit(
            'rev_num(num_1000)',
            setup='from __main__ import rev_num, num_1000',
            number=10000))
print (timeit(
            'rev_num(num_10000)',
            setup='from __main__ import rev_num, num_10000',
            number=10000))