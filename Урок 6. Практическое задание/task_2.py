"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""

# Вариантов много, в принципе многие описаны в презентации к уроку
# мемоизация, кеширование, yield, сжатие данных, сериализация и т.д.
# Пример с yield:

from memory_profiler import profile
import random


@profile
def func_1(count: int):
    for element in range(count):
        yield element


@profile
def func_2(count: int):
    return list(el for el in range(count))


@profile
def enumerate1(func):
    for el in func:
        el_1 = el


enumerate1(func_1(100000))

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     25     18.9 MiB     18.9 MiB           1   @profile
#     26                                         def enumerate1(func):
#     27     18.9 MiB      0.0 MiB      100001       for el in func:
#     28     18.9 MiB      0.0 MiB      100000           el_1 = el

list1 = func_2(100000)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     22     19.0 MiB     19.0 MiB           1   @profile
#     23                                         def func_2(count: int):
#     24     23.3 MiB      4.3 MiB      200003       return list(el for el in range(count))

enumerate1(list1)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     27     18.9 MiB     18.9 MiB           1   @profile
#     28                                         def enumerate1(func):
#     29     18.9 MiB      0.0 MiB      100001       for el in func:
#     30     18.9 MiB      0.0 MiB      100000           el_1 = el

'''
Вывод: очевидно yield очень сильно экономит память, ввиду того, что сборщик мусора успевает периодически очищать память,
которая была выделена на элементы во время перебора.
'''
