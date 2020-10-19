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

import math
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»
    O(n**2)
    """
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


def eratosthenes(inp_num):
    """O(n log(log n))"""
    a = []
    number_count = 0
    num = 2
    while number_count <= inp_num:
        number_count = num / math.log(num)
        num += 1
    for x in range(num + 1):
        a.append(x)

    a[1] = 0
    x = 2
    while x <= num:
        if a[x] != 0:
            y = x + x
            while y <= num:
                a[y] = 0
                y = y + x
        x += 1
    a = [value for value in a if value != 0]
    return a[inp_num - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(f"simple: {timeit('simple(i)', setup='from __main__ import simple, i', number=100)}")
print(eratosthenes(i))
print(f"eratosthenes: {timeit('eratosthenes(i)', setup='from __main__ import eratosthenes, i', number=100)}")

"""Чем выше номер искомого числа тем эффективнее себя проявляет метод «Решета Эратосфена»"""
