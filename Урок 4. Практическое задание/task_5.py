"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
import timeit
import itertools


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


# Вычсисление n-ого простого числа с использованием «Решета Эратосфена»

def primes():
    yield 2
    yield 3
    yield 5
    yield 7
    ps = (p for p in primes())  # поставляем следующие простые числа
    p = next(ps) and next(ps) # не берем 2, берем 3
    q = p * p  # квадрат следующего простого числа
    sieve = {}  # добавляем в словарь простых чисел
    n = 9
    while True:
        if n not in sieve:
            if n < q:
                yield n
            else:
                add(sieve, q + 2 * p, 2 * p)  # n==p*p: for prime p, under p*p + 2*p
                p = next(ps) # add 2*p as incremental step
                q = p * p
        else:
            s = sieve.pop(n)
            add(sieve, n + s, s)
        n += 2  # работа с четными числами


def add(sieve, next, step):
    while next in sieve:  # обеспечиваем уникальность чисел
        next += step
    sieve[next] = step


def primes_up_to(limit):
    return list(itertools.takewhile(lambda p: p <= limit, primes()))


def simple_eratosthenes(n):
    return next(pnum for index, pnum in enumerate(primes()) if index == n - 1)


# i = int(input('Введите порядковый номер искомого простого числа: '))

for i in [10, 100, 1000]:

    print (f'вводим число {i}')
    print(simple(i))
    print(simple_eratosthenes(i))

    print(timeit.timeit("simple(i)", setup="from __main__ import simple, i", number=1000))
    print(timeit.timeit("simple_eratosthenes(i)", setup="from __main__ import simple_eratosthenes, i", number=1000))
    print()

'''
вводим число 10
29
29
0.0864241
0.010182800000000006

вводим число 100
541
541
2.9334577
0.15775400000000017

вводим число 1000
7919
7919
750.3707025
2.318633400000067

Алгоритм с использованием "Решета Эратосфена" намного эффективнее. Чем больше порядковый номер числа, тем больше
разрыв в скорости приведенных выше вариантов вычисления.

Сложность решил прикинуть через регрессионный анализ на сайте https://planetcalc.com/5992/

(1) по первой функции - стопроцентная корреляция с квадратичной функцией (между введеным числом и скоростью вычисления):
y=0.0008x2−0.0571x+0.5770
Correlation coefficient: 1
Сложность первой фукнции выглядит как O(n^2) - квадратичная
https://www.wolframalpha.com/input/?i=y%3D0.0008x2%E2%88%920.0571x%2B0.5770

(2) по второй функции - стопроцентная корреляция с линейной функцией:
y=0.0016x−0.0054
Correlation coefficient: 1
Сложность второй функции выглядит как O(N) - линейная
https://www.wolframalpha.com/input/?i=y%3D0.0000x2%2B0.0016x%E2%88%920.0054
'''