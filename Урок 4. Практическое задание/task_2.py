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
        return ''  # тут добавлялся лишний ноль в конце реверсивной строки
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
            # print(cache[args])
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


def slice_reverse_mem(number):
    return str(number)[::-1]


def for_reverse_mem(number):
    result = ''
    while number > 1:
        result += str(number % 10)
        number = number // 10
    return result


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


print('Оптимизированная функция for_reverse_mem')
print(
    timeit(
        'for_reverse_mem(num_100)',
        setup='from __main__ import for_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'for_reverse_mem(num_1000)',
        setup='from __main__ import for_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'for_reverse_mem(num_10000)',
        setup='from __main__ import for_reverse_mem, num_10000',
        number=10000))

print('Оптимизированная функция slice_reverse_mem')
print(
    timeit(
        'slice_reverse_mem(num_100)',
        setup='from __main__ import slice_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'slice_reverse_mem(num_1000)',
        setup='from __main__ import slice_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'slice_reverse_mem(num_10000)',
        setup='from __main__ import slice_reverse_mem, num_10000',
        number=10000))


"""
Мемоизация здесь сильно помогла, скорость повысилась на порядок, за счет сохранения результатов предыдущих операций 
в кеше 
Через цикл получилось быстрее  чем просто рекурсия, но медленей чем мемеоизированая рекурсия
Решение через срез по скорости почти не уступает мемоизированой рекурсии.

"""
