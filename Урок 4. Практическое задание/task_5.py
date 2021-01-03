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
    """Без использования «Решета Эратосфена»
        Сложность n^2
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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


def func(num):
    """Сложность n(log(nlogn))"""
    n = 10000
    my_list = [i for i in range(n + 1)]
    my_list[1] = 0
    i = 2

    while i <= n:
        if my_list[i] != 0:
            j = i + i
            while j <= n:
                my_list[j] = 0
                j = j + i
        i += 1

    my_set = set(my_list)
    my_set.remove(0)
    my_list = list(my_set)
    my_list.sort()

    return my_list[num - 1]


num = int(input('Введите порядковый номер искомого простого числа: '))
print(func(num))

# для числа 10
print("Для числа 10")
print(timeit(
    'simple(10)',
    setup='from __main__ import simple',
    number=10000))

print(timeit(
    'func(10)',
    setup='from __main__ import func',
    number=10000))

# для числа 100
print("Для числа 100")
print(timeit(
    'simple(100)',
    setup='from __main__ import simple',
    number=10000))

print(timeit(
    'func(100)',
    setup='from __main__ import func',
    number=10000))

# для числа 1000
print("Для числа 1000")
print(timeit(
    'simple(1000)',
    setup='from __main__ import simple',
    number=10000))

print(timeit(
    'func(1000)',
    setup='from __main__ import func',
    number=10000))

"""
1-й алгоритм эффективен для небольших чисел, т.к. с увелечением числа возрастает время выполнения. 
Решение через алгоритм "Решето эратосфена" выполняется приблизительно одинаково для любых чисед.
"""