"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile



# Если мы рекурсивно вызываем функцию, то на каждый вызов будет отображена таблица затрат памяти
# чтобы этого избежать, мы можем поместить вызов функции в другую функцию, обрамив ее декоратором

# @profile
def factorial(n):
    if n == 0:
        return 0
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res + factorial(n-1)

# factorial(10)

@profile
def easy_to_profile(n):
    return factorial(n)

easy_to_profile(777)

#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     27     15.6 MiB     15.6 MiB           1   @profile
#     28                                         def easy_to_profile(n):
#     29     16.3 MiB      0.7 MiB           1       return factorial(n)
#
