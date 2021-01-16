"""Необходимо сделать профилировку скрипта с рекурсией
Возьмем скрипт с факториалом"""
"""На каждый вызов функции открывается своя таблица,
попробуем положить реверсивную функцию в другую функцию"""
from memory_profiler import profile


def fact(numb):
    if numb == 0:
        return 1
    else:
        return numb * fact(numb - 1)


@profile
def new_func(n):
    return fact(n)


print(new_func(600))

"""Дополнение к заданию 1. Сравним с решением через цикл"""


@profile
def fact_cycle(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(fact_cycle(600))


"""Результаты для рекурсии:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    15     16.0 MiB     16.0 MiB           1   @profile
    16                                         def new_func(n):
    17     16.5 MiB      0.5 MiB           1       return fact(n)
    
Результаты для цикла:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    25     16.5 MiB     16.5 MiB           1   @profile
    26                                         def fact_cycle(n):
    27     16.5 MiB      0.0 MiB           1       result = 1
    28     16.5 MiB      0.0 MiB         601       for i in range(1, n + 1):
    29     16.5 MiB      0.0 MiB         600           result *= i
    30     16.5 MiB      0.0 MiB           1       return result

Решение через рекурсию занимает больше памяти, т.к. вызовы функции сохраняются в стеке
"""