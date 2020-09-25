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
        return ''
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


def my_func_reverse(number):
    my_reverse = list(str(number))
    my_reverse.reverse()
    return ''.join(my_reverse)


def my_func_reverse_2(number):
    my_reverse = str(number)
    return my_reverse[::-1]


print('Мой вариант оптимизации 1:')
print(
    timeit(
        "my_func_reverse(num_100)",
        setup="from __main__ import my_func_reverse, num_100",
        number=10000
    ))
print(
    timeit(
        "my_func_reverse(num_1000)",
        setup="from __main__ import my_func_reverse, num_1000",
        number=10000
    ))
print(
    timeit(
        "my_func_reverse(num_10000)",
        setup="from __main__ import my_func_reverse, num_10000",
        number=10000
))

print('Мой вариант оптимизации 2:')
print(
    timeit(
        "my_func_reverse_2(num_100)",
        setup="from __main__ import my_func_reverse_2, num_100",
        number=10000
    ))
print(
    timeit(
        "my_func_reverse_2(num_1000)",
        setup="from __main__ import my_func_reverse_2, num_1000",
        number=10000
    ))
print(
    timeit(
        "my_func_reverse_2(num_10000)",
        setup="from __main__ import my_func_reverse_2, num_10000",
        number=10000
))
"""
Из результатов замеров видно, что мемоизация нужна, благодоря ей вычисления происходят гораздо быстрее,
т.к. она хранит результаты вычислений в словаре.
Я попробовал оптимизировать программу за счет встроенных функций. Получилось значительно лучше, чем
первоначальный вариант, но хуже варианта с мемоизацией.
Вывод:
Не оптимизированная фун-я: просто рекурсия это большие затраты времени
Оптимизация-мемоизация: Самый быстрый вариант, т.к. хранит результаты вычислений в хеш таблице, 
с доступом по времени О(1).
Мои варианты: хорош тем, что используются стандартные отлично работающие фун-ии и срезы,
но все равно их сложность O(n).
"""
