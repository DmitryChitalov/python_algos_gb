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
import sys


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

sys.setrecursionlimit(10000)
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


def reverse_cycle(number):
    rev_num = ''
    while number != 0:
        rev_num += str(number % 10)
        number //= 10
    return rev_num


print('Работа функции reverse_cycle')
print(
    timeit(
        'reverse_cycle(num_100)',
        setup='from __main__ import reverse_cycle, num_100',
        number=10000))
print(
    timeit(
        'reverse_cycle(num_1000)',
        setup='from __main__ import reverse_cycle, num_1000',
        number=10000))
print(
    timeit(
        'reverse_cycle(num_10000)',
        setup='from __main__ import reverse_cycle, num_10000',
        number=10000))


def main():
    recursive_reverse(num_10000)
    recursive_reverse_mem(num_10000)
    reverse_cycle(num_10000)


"""
Сделал свой вариант через цикл
Через цикл выполняется в 1.5 раза быстрее, чем через рекурсию,
И через мемоизацию время выполнения фактически не зависит от кол-ва элементов, это понятно, потому что она уже расчитана
ранее.
Вывод: мемоизация здесь нужна

P.S. надеюсь я правильно понял мемоизацию, было очень много эксперементов)
"""