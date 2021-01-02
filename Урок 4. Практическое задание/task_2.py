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
from timeit import Timer

number = 123456789


def memorize(func):
    def g(number, memory = {}):
        r = memory.get(number)
        if r is None:
            r = func(number)
            memory[number] = r
        return r
    return g


def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


print(fib(20))


@memorize
def recursive_reverse(number):
    if number == 1:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print(recursive_reverse(number))

print(timeit.timeit("recursive_reverse(number)", setup="from __main__ import recursive_reverse, number"))


