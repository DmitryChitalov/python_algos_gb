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


def eratosthenes(foo):
    n=10000
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    a = list(a)
    a.sort()
    return a[foo-1]

# i = int(input('Введите порядковый номер искомого простого числа: '))
i=1000

print(simple(i))
print(eratosthenes(i))

print(timeit("simple(i)", setup="from __main__ import simple, i", number=10))
print(timeit("eratosthenes(i)", setup="from __main__ import eratosthenes, i", number=10))

'''
i=10
simple -       0.0003437999999999983
eratosthenes - 0.0914269

i=100
simple -       0.04156
eratosthenes - 0.0855018

i=1000
simple -       7.6530222000000006
eratosthenes - 0.07896700000000045


Для решения этой задачи взял код предложенный на сайте и немного его переделал.
Проблемма данного решения заключается в необходимости генерировать большой массив данных в самом начале.
Я считаю это не оптимальным. 
"Решето эратосфена"  выигрывает на больших значениях, скорость его работы O(N logN) учитывая что sort() тоже имеет 
сложность O(N logN), а скорость работы через перебор делителей O(N^2)
'''