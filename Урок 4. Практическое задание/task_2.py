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
Не оптимизированная функция recursive_reverse
0.0206328
0.0262581
0.04792719999999999
0.051870200000000005
Оптимизированная функция recursive_reverse_mem
0.0017052000000000178
0.0017710000000000226
0.0017722000000000016
0.0017844999999999944
0.031245599999999984
0.024072499999999997
0.6601693
0.0034925000000000095
С одной стороны, оптимизация имеет смысл так как сложность становится практически константой 
(время выполнения изменяется незначительно, вне зависимости от размера числа)
и позволяет избавиться от лишних рекурсивных вызовов. С другой - наиболее эффективна 
реализация переводом в строку и выводом в обратном порядке, и с этой точки зрения можно 
сказать что излишние затраты памяти на словарь не имеют смысла 
"""
from timeit import timeit
from random import randint

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

def iter_reverse_1(number):
    res = ''
    cache = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    while number > 10:
        res += cache.get( number % 10 )
        number = number // 10
    res += cache.get( number )
    return res

def iter_reverse_2(number):
    res = ''
    cache = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while number > 10:
        res += cache[ number % 10 ]
        number = number // 10
    res += cache[ number ]
    return res

def iter_reverse_3(number):
    res = 0
    while number > 0:
        res *= 10
        res += number % 10
        number /= 10
    return res

def str_reverse(number):
    return (str(number))[::-1]

num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
num_10000000 = randint(100000000000, 10000000000000000)

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
print(
    timeit(
        "recursive_reverse(num_10000000)",
        setup='from __main__ import recursive_reverse, num_10000000',
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
print(
    timeit(
        'recursive_reverse_mem(num_10000000)',
        setup='from __main__ import recursive_reverse_mem, num_10000000',
        number=10000))

print(
    timeit(
        'iter_reverse_1(num_10000000)',
        setup='from __main__ import iter_reverse_1, num_10000000',
        number=10000))

print(
    timeit(
        'iter_reverse_2(num_10000000)',
        setup='from __main__ import iter_reverse_2, num_10000000',
        number=10000))
print(
    timeit(
        'iter_reverse_3(num_10000000)',
        setup='from __main__ import iter_reverse_3, num_10000000',
        number=10000))
print(
    timeit(
        'str_reverse(num_10000000)',
        setup='from __main__ import str_reverse, num_10000000',
        number=10000))
