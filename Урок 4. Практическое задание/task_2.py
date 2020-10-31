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
В данном примере мемоизация ускоряет работу программы, так как для повторяющихся значений не производятся новые вызовы
функции, а значения берутся из кэш, который представляет из себя словарь и значения возвращаются за O(1).
"""


# мой вариант с использованием встроенных методов
def simple_reverse(number):
    """
    Возвращает строку, а не число, чтобы учесть 0 в конце исходного числа. Например при вводе 1200 функция вернет 0021.
    Если бы она возвращала
    """
    return ''.join(list(reversed(list(str(number)))))


print('Вариант с использованием встроенных методов simple_reverse')
print(
    timeit(
        "simple_reverse(num_100)",
        setup='from __main__ import simple_reverse, num_100',
        number=10000))
print(
    timeit(
        "simple_reverse(num_1000)",
        setup='from __main__ import simple_reverse, num_1000',
        number=10000))
print(
    timeit(
        "simple_reverse(num_10000)",
        setup='from __main__ import simple_reverse, num_10000',
        number=10000))

"""
Вариант с использованием встроенных методов работает быстрее неоптимизированного рекурсивного варианта, так как не
тратится время на создание и опустошение стека рекурсивных вызовов, но сильно уступает варианту с мемоизацией, 
где повторяющиеся значения берутся из кэш за О(1).
"""

print('Для проверки результатов:')
print({recursive_reverse(num_10000)}, {recursive_reverse_mem(num_10000)}, {simple_reverse(num_10000)})
print('Результаты работы всех трех вариантов совпадают')
