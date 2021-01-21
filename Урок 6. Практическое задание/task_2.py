"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""

from memory_profiler import profile
import random
from functools import reduce


@profile
def pgm():
    """
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
        10     19.0 MiB     19.0 MiB           1   @profile
        11                                         def pgm():
        12     20.4 MiB      1.4 MiB       50003       a = [random.randint(-100, 100) for _ in range(50000)]
        13     20.4 MiB      0.0 MiB           1       new_arr = []
        14
        15     21.1 MiB      0.6 MiB       50001       for item in a:
        16     21.1 MiB      0.0 MiB       50000           if item % 2 == 0:
        17     21.1 MiB      0.0 MiB       25145               new_arr.append(pow(item, 2))
        18
        19     21.1 MiB      0.0 MiB           1       return new_arr
    """
    a = [random.randint(-100, 100) for _ in range(50000)]
    new_arr = []

    for item in a:
        if item % 2 == 0:
            new_arr.append(pow(item, 2))

    return new_arr


pgm()

""" Испоьзование генераторных выражений """


@profile
def pgm2():
    """
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
        39     19.1 MiB     19.1 MiB           1   @profile
        40                                         def pgm2():
        41     21.1 MiB     -0.0 MiB      100005       new_arr = [pow(i, 2) for i in [random.randint(-100, 100) for _ in range(50000)] if i % 2 == 0]
        42     20.1 MiB     -1.0 MiB           1       return new_arr
        """
    new_arr = [pow(i, 2) for i in [random.randint(-100, 100) for _ in range(50000)] if i % 2 == 0]
    return new_arr


pgm2()

""" Испоьзование yield """


@profile
def pgm3():
    """
    Memory_profile не дает результат
    """
    for item in range(50000):
        if item % 2 == 0:
            yield pow(item, 2)


pgm3()

"""Использовать map для обработки списка"""


@profile
def prm():
    """
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
        76     18.9 MiB     18.9 MiB           1   @profile
        77                                         def prm():
        78     20.4 MiB      1.5 MiB       50003       a = [random.randint(-100, 100) for _ in range(50000)]
        79     20.4 MiB      0.0 MiB           1       new_arr = []
        80
        81     22.1 MiB      1.3 MiB       50001       for i in a:
        82     22.1 MiB      0.4 MiB       50000           new_arr.append(i ** 2)
        83
        84     22.1 MiB      0.0 MiB           1       return new_arr
        """
    a = [random.randint(-100, 100) for _ in range(50000)]
    new_arr = []

    for i in a:
        new_arr.append(i ** 2)

    return new_arr


@profile
def prm2():
    """
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
        99     19.1 MiB     19.1 MiB           1   @profile
       100                                         def prm2():
       101     20.8 MiB      1.8 MiB       50003       a = [random.randint(-100, 100) for _ in range(50000)]
       102     20.8 MiB      0.0 MiB           1       map(lambda x: x**2, a)
       103
       104     20.8 MiB      0.0 MiB           1       return a
    """
    a = [random.randint(-100, 100) for _ in range(50000)]
    map(lambda x: x ** 2, a)

    return a


print(prm())
print(prm2())
