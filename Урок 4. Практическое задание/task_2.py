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
        return '' # str(number % 10) -> исправлен код, функция добавляла 0 в конце реверса.
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


def reverse(number):
    rev_number = str(number)[::-1]
    return rev_number

print('Реверс через строку reverse')
print(timeit('reverse(num_100)', globals=globals(), number=10000))
print(timeit('reverse(num_1000)', globals=globals(), number=10000))
print(timeit('reverse(num_10000)', globals=globals(), number=10000))

"""
Результаты замеров:
Не оптимизированная функция recursive_reverse
0.026580600000000003
0.02971130000000001
0.0606825

Оптимизированная функция recursive_reverse_mem
0.0024153999999999842
0.00273000000000001
0.0033473000000000253

После мемоизации время значительно сократилось.
Попыталась решить задачу через ревес строк (результаты замеров ниже). 
Время выполнения гораздо ниже чем при рекурсии, но все равно уступают мемоизации.
Мемоизация в данной задаче оправдана.  

Реверс через строку reverse
0.004578500000000013
0.005385799999999996
0.004432400000000003
"""