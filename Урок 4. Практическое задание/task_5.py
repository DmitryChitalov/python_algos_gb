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

'''Сложность: O(n**2)'''


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:  # O(n)
        t = 1
        is_simple = True
        while t <= n:  # O(n)
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


"""Менее эффективно чем наивный алгоритм т.к. здесь формируется огромный список, а затем его значения удаляются
    А у наивного алгоритнма количество итераций ограниченно искомым числом"""


def simple2(inp_num):
    a = []
    number_of_primes = 0
    num = 2
    while number_of_primes <= inp_num:
        number_of_primes = num / math.log(num)
        num += 1
    for i in range(num + 1):
        a.append(i)

    a[1] = 0
    i = 2
    while i <= num:
        if a[i] != 0:
            j = i + i
            while j <= num:
                a[j] = 0
                j = j + i
        i += 1
    a = [value for value in a if value != 0]
    return a[inp_num - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple2(i))
print(simple(i))
print(timeit('simple2(i)', setup='from __main__ import simple2, i', number=10))
print(timeit('simple(i)', setup='from __main__ import simple, i', number=10))
