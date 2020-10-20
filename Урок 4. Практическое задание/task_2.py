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

import timeit


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


number = 1000

print(timeit.timeit("recursive_reverse(number)", setup="from __main__ import recursive_reverse, number"))


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
def recursive_reverse__1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse__1(number // 10)}'


print(timeit.timeit("recursive_reverse__1(number)", setup="from __main__ import recursive_reverse__1, number"))
"""
Используя мемоизацию скорость программы увеличилась
"""
