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


def reverse_str(number):
    return str(number)[::-1]


print('Новая функция reverse_str')
print(
    timeit(
        'reverse_str(num_100)',
        setup='from __main__ import reverse_str, num_100',
        number=10000))
print(
    timeit(
        'reverse_str(num_1000)',
        setup='from __main__ import reverse_str, num_1000',
        number=10000))
print(
    timeit(
        'reverse_str(num_10000)',
        setup='from __main__ import reverse_str, num_10000',
        number=10000))



"""Была добавлена новая функция reverse_str, которая обращает число в str и выводит как перевернутую строку.
   Данный алгоритм значительно быстрее, чем алгоритм первой функции recursive_reverse, а также занимает всего
   одну строку, но все равно он немного уступает по скорости алгоритму функции recursive_reverse_mem, которая 
   использует мемоизацию. Данный алгоритм еще раз доказывает, как важно использовать мемоизацию при работе с 
   рекурсиями: если значение уже содержится в кеше, то повторное его вычисление проводиться не будет, вместо
   этого будет возвращено имеющееся значение. """
