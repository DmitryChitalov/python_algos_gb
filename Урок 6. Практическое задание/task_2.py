"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""


import random
from memory_profiler import profile


def list_gen(length):
    for i in range(length):
        yield random.randint(0, 5000)


@profile
def test():
    lst = list_gen(100000)
    min = 0
    for i in lst:
        if i < min:
            min = i


@profile
def test_2():
    lst = [el for el in list_gen(100000)]
    min = 0
    for i in lst:
        if i < min:
            min = i


test()
test_2()


"""
Используя генератор память не расходуется на хранение списка:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     8     18.7 MiB     18.7 MiB           1   @profile
     9                                         def test():
    10     18.7 MiB      0.0 MiB           1       lst = list_gen(100000)
    11     18.7 MiB      0.0 MiB           1       min = 0
    12     18.7 MiB      0.0 MiB      100001       for i in lst:
    13     18.7 MiB      0.0 MiB      100000           if i < min:
    14                                                     min = i
    
Если массив, то расходуется:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    25     18.7 MiB     18.7 MiB           1   @profile
    26                                         def test_2():
    27     23.7 MiB      5.0 MiB      100003       lst = [el for el in list_gen(100000)]
    28     23.7 MiB      0.0 MiB           1       min = 0
    29     23.7 MiB      0.0 MiB      100001       for i in lst:
    30     23.7 MiB      0.0 MiB      100000           if i < min:
    31                                                     min = i

"""