"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
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

# добавил декоратор с мемоизацией
