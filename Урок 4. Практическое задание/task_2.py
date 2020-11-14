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

'''
При каждом шаге рекурсии в кеш записывается часть пройденного числа (к качестве ключа) и
она же, но пропущенная через функцию переворачивания (в качестве значения). Кеш помогает
здесь составить новое значение на основе предыдущего, поэтому мемоизация в этой реализации
полезна.

Ускорения удалось добиться путём передачи в рекуривную функцию с мемоизацией последнего символа в строке
с числом, где сам символ вычленяется при помощи индекса [-1], одновременно отрезая его у передаваемой в 
функцию строки.
'''


def memorize_mk2(func):
    def wrapper(input_str, output_str='', memory={}):
        if memory is None:
            memory = {}
        result = memory.get(input_str)
        if result is None:
            result = func(input_str, output_str)
            memory[input_str] = result
        return result

    return wrapper


@memorize_mk2
def recursive_reverse_mem_mk2(input_str, output_str=''):
    if not isinstance(input_str, str):
        input_str = str(input_str)
    if len(input_str) > 0:
        return recursive_reverse_mem_mk2(input_str[:-1], output_str + input_str[-1])
    else:
        return output_str


print(f'\nОптимизированная функция recursive_reverse_mem_mk2')
print(
    timeit(
        'recursive_reverse_mem_mk2(num_100)',
        setup='from __main__ import recursive_reverse_mem_mk2, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_mk2(num_1000)',
        setup='from __main__ import recursive_reverse_mem_mk2, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_mk2(num_10000)',
        setup='from __main__ import recursive_reverse_mem_mk2, num_10000',
        number=10000))
