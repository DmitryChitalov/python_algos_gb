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
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:  # O(N)
        t = 1
        is_simple = True
        while t <= n:  # O(N)
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n  # O(N**2)


def simple_re(n, i_max):
    a = []
    for i in range(i_max + 1):  # O(N)
        a.append(i)
    a[1] = 0
    i = 2
    while i <= i_max:  # O(N)
        if a[i] != 0:
            j = i + i
            while j <= i_max:  # O(N)
                a[j] = 0
                j = j + i
        i += 1

    a = set(a)
    a.remove(0)
    return sorted(a)[n - 1]  # O(N**2)


def prime_counting_function(i):
    """ Функция возвращает верхнюю границу отрезка на котором лежат
    i-e количество простых чисел. Функция основана на теореме о
    распределении простых чисел, она утверждает, что функция
    распределения простых чисел. Количество простых чисел на отрезке
    [1;n] растёт с увеличением n как n / ln(n).
    """

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


i = int(input('Введите порядковый номер искомого простого числа: '))
i_max = prime_counting_function(i)

"""Порядок времени выполнения обоих алгоритмов одинаков, но на практике наивный алгоритм работает быстрее
при данной постановке задачи. Количество итераций внутренних циклов у него ограничено номером искомого числа,
в то время, как второму алгоритму нужно сформировать массив, длинна которого значительно больше этого числа 
и увеливается в геометрической прогрессии при увеличении числа. Кроме того, эту длину нужно еще и вычислить."""
