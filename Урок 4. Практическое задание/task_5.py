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

from timeit import timeit


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


i_10 = 10
i_100 = 100
i_1000 = 1000

print(timeit('simple(i_10)',
             setup='from __main__ import simple, i_10',
             number=10000))
print(timeit('simple(i_100)',
             setup='from __main__ import simple, i_100',
             number=10000))
print(timeit('simple(i_1000)',
             setup='from __main__ import simple, i_1000',
             number=10000))

"""
    С увеличением числа, время так же увеличивается, причем многократно.
    Последнее время, i_1000, программа так и не вывела, так как я остановил работу,
    прошло больше 2-х минут. 
"""







