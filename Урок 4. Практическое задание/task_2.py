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
Мемоизация дает прирост скорости на порядок. Так же при использовани мемоизации скорость выполнения 
практически не зависит от длины входного числа. Соответственно мемоизация здесь нужна. 


Замерим скорость решений без использования рекурсии:
"""


def reverse_num(num):
    return int(str(num)[::-1])

def reverse_num2(num):
    reverse_num = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        reverse_num = reverse_num * 10
        reverse_num = reverse_num + digit
    return reverse_num


print('Классическое решение: ')
print(timeit(
    'reverse_num2(num_100)',
    setup='from __main__ import reverse_num2, num_100',
    number=10000))
print(timeit(
    'reverse_num2(num_1000)',
    setup='from __main__ import reverse_num2, num_1000',
    number=10000))
print(timeit(
    'reverse_num2(num_10000)',
    setup='from __main__ import reverse_num2, num_10000',
    number=10000))

print('Решение через срез строки: ')
print(timeit(
    'reverse_num(num_100)',
    setup='from __main__ import reverse_num, num_100',
    number=10000))
print(timeit(
    'reverse_num(num_1000)',
    setup='from __main__ import reverse_num, num_1000',
    number=10000))
print(timeit(
    'reverse_num(num_10000)',
    setup='from __main__ import reverse_num, num_10000',
    number=10000))

"""
Решение через срез строки работает быстро, но почти вдвое медленее, чем решение через рекурсию 
с использованием мемоизации
"""