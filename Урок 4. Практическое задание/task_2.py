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
234
def reverse(number):
    res = 0
    for i in range(len(number)):
        res += (number % 10)*10
        number = number // 10
    return res

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

num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

def rev(num):
    res = 0
    for i in range(len(str(num))):
        digit = num % 10
        num = num // 10
        res = res * 10
        res = res +  digit
    return res


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Моя оптимизированная функция rev')
print(
    timeit(
        "rev(num_100)",
        setup='from __main__ import rev, num_100',
        number=10000))
print(
    timeit(
        "rev(num_1000)",
        setup='from __main__ import rev, num_1000',
        number=10000))
print(
    timeit(
        "rev(num_10000)",
        setup='from __main__ import rev, num_10000',
        number=10000))

def rev_lst(num):
    num = str(num)
    n_list = list(num)
    n_list.reverse()
    n2 = "".join(n_list)
    return n2

num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Моя оптимизированная функция_2 rev_lst')
print(
    timeit(
        "rev_lst(num_100)",
        setup='from __main__ import rev_lst, num_100',
        number=10000))
print(
    timeit(
        "rev_lst(num_1000)",
        setup='from __main__ import rev_lst, num_1000',
        number=10000))
print(
    timeit(
        "rev_lst(num_10000)",
        setup='from __main__ import rev_lst, num_10000',
        number=10000))


def rev_str(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

enter_num_100 = randint(10000, 1000000)
enter_num_1000 = randint(1000000, 10000000)
enter_num_10000 = randint(100000000, 10000000000000)


print('Моя оптимизированная функция_3 rev_str')
print(
    timeit(
        "rev_str(enter_num_100)",
        setup='from __main__ import rev_str, enter_num_100',
        number=10000))
print(
    timeit(
        "rev_str(enter_num_1000)",
        setup='from __main__ import rev_str, enter_num_1000',
        number=10000))
print(
    timeit(
        "rev_str(enter_num_1000)",
        setup='from __main__ import rev_str, enter_num_1000',
        number=10000))

#Смысла в дальнейшей оптимизации нет, вариант решения через мемоизацию самый оптимальный и быстрый.
