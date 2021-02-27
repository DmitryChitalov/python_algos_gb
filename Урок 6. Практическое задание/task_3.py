"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile
import sys
sys.setrecursionlimit(2147483647)


def sum_recursive(lst: list):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_recursive(lst[1:])


@profile
def wrapper_summ(lst: list):
    sum_recursive(lst)


@profile
def summ(lst: list):
    return sum(lst)

list1 = [el for el in range(1500)]
wrapper_summ(list1)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     20     19.0 MiB     19.0 MiB           1   @profile
#     21                                         def wrapper_summ(lst: list):
#     22     21.7 MiB      2.7 MiB           1       sum_recursive(lst)

summ(list1)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     25     18.8 MiB     18.8 MiB           1   @profile
#     26                                         def summ(lst: list):
#     27     18.8 MiB      0.0 MiB           1       return sum(lst)

'''
Выводы:
    1)для профилирования рекурсивных функций создаём обёртку и профилируем её.
    2)способ с рекурсией хуже как минимум ввиду намного меньшего потребления памяти и опасности переполнения стека.
'''
