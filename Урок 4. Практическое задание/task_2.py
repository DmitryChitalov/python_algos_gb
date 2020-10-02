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

# Результаты замеров показывают, что мемоизация нужна и полезна, так как сокращает время больше чем в 10 раз.
# с точки зрения алгоритмов мемоизация тоже нужна: в больших числах часто встречаются комбинации цифр,
# которые мы уже вычисляли. Нет смысла вычислять их ещё раз - лучше забирать их из словаря.
# Доступ к значению по ключу займет меньше времени чем очередная рекурсия.





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
        if args not in cache:
            #return cache[args]
        #else:
            cache[args] = f(*args)
        return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print(f'Оптимизированная функция recursive_reverse_mem')
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


# Из улучшений я придумал только одно:
# убрать дублирование return  в декораторе и переписать его так:


def memoize_2(f):
    cache = {}

    def decorate(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return decorate

# замеры показывают, что немного выиграли (но чисто символически).


@memoize_2
def recursive_reverse_mem_2(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem_2(number // 10)}'

print(f'Финально оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem_2(num_100)',
        setup='from __main__ import recursive_reverse_mem_2, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_2(num_1000)',
        setup='from __main__ import recursive_reverse_mem_2, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_2(num_10000)',
        setup='from __main__ import recursive_reverse_mem_2, num_10000',
        number=10000))

