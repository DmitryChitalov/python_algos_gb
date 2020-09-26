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
print(f'1- {num_100}')
num_1000 = randint(1000000, 10000000)
print(f'2- {num_1000}')
num_10000 = randint(100000000, 10000000000000)
print(f'3- {num_10000}')

print(f'1-  {recursive_reverse(num_100)}, 2-  {recursive_reverse(num_1000)}, 3-  {recursive_reverse(num_10000)}')

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


print(f'1-  {recursive_reverse_mem(num_100)}, 2-   {recursive_reverse_mem(num_1000)}, 3-   {recursive_reverse_mem(num_10000)}' )
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


def my_version(number):
    number_reverse = str(number)
    # return ''.join(reversed(str(number)))
    return number_reverse[::-1]



print(my_version(num_10000))
print(
    timeit(
        'my_version(num_10000)',
        setup='from __main__ import my_version, num_10000',
        number=10000))



"""замеры времени показывают, что мемоизация в данном примере актуальна."""