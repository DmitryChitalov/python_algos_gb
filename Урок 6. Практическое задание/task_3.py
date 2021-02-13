"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


@profile
def decor_fact(n):
    return fact(n)


print(decor_fact(10))

#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     19     37.6 MiB     37.6 MiB           1   @profile
#     20                                         def decor_fact(n):
#     21     37.6 MiB      0.0 MiB           1       return fact(n)
#
#
# 3628800
#
# Для профилирования рекурсивной фукции ее вызов необходимо "обернуть" в еще
# одну функцию
