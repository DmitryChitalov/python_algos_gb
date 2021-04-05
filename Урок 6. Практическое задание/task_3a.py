"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from itertools import tee, islice
from operator import add
from timememit import timememit
import sys


# Сначала профилируем простую рекурсивную функцию
@timememit
def fib_rec(n_val):
    def func(n_val):
        if n_val < 2:
            return n_val
        return func(n_val - 1) + func(n_val - 2)
    return func(n_val)


print(fib_rec(40))
# ---
# fib_rec: 30.7462 s, 0.000000 MiB
# 102334155
# ---


def memoize(func):
    def wrapper(n_val, memory={}):
        res = memory.get(n_val)
        if res is None:
            res = func(n_val)
            memory[n_val] = res
        return res
    return wrapper


# Теперь с мемоизацией
@timememit
def fib_rec_mem(n_val):
    @memoize
    def func(n_val):
        if n_val < 2:
            return n_val
        return func(n_val - 1) + func(n_val - 2)
    return func(n_val)


print(f'f(1) : {fib_rec_mem(1)}')
print(f'f(100) : {fib_rec_mem(100)}')
# ---
# fib_rec_mem: 0.1011 s, 0.000000 MiB
# f(1) : 1
# fib_rec_mem: 0.1014 s, 0.000000 MiB
# f(100) : 354224848179261915075
# ---
# Как будто f(1) выполняется столько же, сколько и f(100),
# чего, конечно, не может быть. Видимо, время выполнения самой
# функции существенно меньше накладных расходов на профилирование.


# Попробуем применить ленивые вычисления.
# С помощью itertools можно сделать рекурсивный генератор
# чисел Фибоначчи, который соответствует коду на Haskell
# fibs = 1 : 1 : zipWith (+) fibs (tail fibs)
# идея взята отсюда
# https://joelgrus.com/2015/07/07/haskell-style-fibonacci-in-python/
def lazy_fibs():
    yield 1
    yield 1
    fibs1, fibs2 = tee(lazy_fibs())
    # генератор суммируется со своей копией,
    # сдвинутой на 1 элемент
    yield from map(add, fibs1, islice(fibs2, 1, None))


@timememit
def fibonacci(n):
    # берем n-ный элемент итератора
    return next(islice(lazy_fibs(), n-1, None))


print(f'f(1) : {fibonacci(1)}')
print(f'f(100) : {fibonacci(100)}')
# ---
# fibonacci: 0.1011 s, 0.000000 MiB
# fibonacci(1) : 1
# fibonacci: 0.1040 s, 0.257812 MiB
# fibonacci(100) : 354224848179261915075
# ---
# Со временем та же ситуация, что и для функции с мемоизацией.
# Однако потребление памяти существенно выросло.
# При этом f(90) все еще потребляет 0 MiB памяти.
print(f'f(90) : {fibonacci(90)}')
# ---
# fibonacci: 0.1034 s, 0.000000 MiB
# fibonacci(90) : 2880067194370816120
# ---
# Резкий скачок потребления памяти после f(90) возможно
# связан с тем, что # элементы последовательности
# больше не умещаются в long long
print(sys.maxsize)
# ---
# 9223372036854775807
# ---
# поэтому старшие члены ряда хранятся в виде bigint, требования
# этого типа к памяти намного больше. У версии с мемоизацией
# этот скачок тоже наступает, но позже
print(f'f(130) : {fib_rec_mem(130)}')
# ---
# fib_rec_mem: 0.1017 s, 0.257812 MiB
# f(130) : 659034621587630041982498215
# ---
# В итоге алгоритм с мемоизацией более эффективен
# и по скорости, и по потреблению памяти, чем алгоритм с
# бесконечным генератором (ленивой последовательностью)
