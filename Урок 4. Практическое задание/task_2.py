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
"""
меморизация нужна только если эта функция вызываеться много раз.
Если же функция вызывается мало смысл в меморизации теряеться так,
как создание хеш-таблицы будет занимать время.
Ниже приведенны данные замера(cProfile) вызова ф-ции с различными аргументами 100_000 раз. Как видем 
экономия времении существенная. Производил замеры также и с использованием timeit. 
Но как я понял timeit производит замеры с одним и тем же аргументом, поэтому для контроля 
воспользовался cProfile.
Попробывал оптимизировать с помощью среза, получаеться экономия времени.
########################################################################################
   ncalls      tottime  percall  cumtime  percall filename:lineno(function)
167222/100000   0.107    0.000    0.173    0.000 tmp.py:14(decorate)
67223/58087     0.067    0.000    0.108    0.000 tmp.py:24(recursive_reverse_mem)
100000          0.053    0.000    0.053    0.000 tmp.py:31(revers_slice)
590767/100000   0.412    0.000    0.412    0.000 tmp.py:5(recursive_reverse)
################################################################################
Результат запуска функций:

58772 - control
277850 - recursive_reverse(x) - Ошибка
27785 - recursive_reverse_mem(x)
27785 - revers_slice(x)
"""

from timeit import timeit
from random import randint

##########################################################################################
"""
мой вариант
"""


def revers_slice(number):
    return str(number)[::-1]

##########################################################################################


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
