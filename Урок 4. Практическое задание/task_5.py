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

def simple(i):

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
"""

from math import log


def brut_len(number):
    _n = 10
    k = _n / log(_n)
    while k < number:
        _n *= 10
        k = _n / log(_n)
    return _n


if __name__ == '__main__':
    n = int(input('Введите порядковый номер искомого простого числа: '))

    cache_len = brut_len(n)
    cache = {i: True for i in range(2, cache_len)}

    count = 0
    p = 2

    simples = []

    while count != n:
        if cache[p]:
            count += 1
            simples.append(p)
            for i in range(2*p, cache_len, p):
                cache[i] = False
        p += 1

    print(simples)
    print(cache)
