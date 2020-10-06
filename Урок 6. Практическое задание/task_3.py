"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile


@profile
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


print(fac(3))
'''
Filename: ~/task_3.py

Line #    Mem usage    Increment   Line Contents
================================================
     7     13.8 MiB     13.8 MiB   @profile
     8                             def fac(n):
     9     13.8 MiB      0.0 MiB       if n == 0:
    10     13.8 MiB      0.0 MiB           return 1
    11                                 return fac(n-1) * n


Filename: ~/task_3.py

Line #    Mem usage    Increment   Line Contents
================================================
     7     13.8 MiB     13.8 MiB   @profile
     8                             def fac(n):
     9     13.8 MiB      0.0 MiB       if n == 0:
    10     13.8 MiB      0.0 MiB           return 1
    11     13.8 MiB      0.0 MiB       return fac(n-1) * n


Filename: ~/task_3.pyy

Line #    Mem usage    Increment   Line Contents
================================================
     7     13.8 MiB     13.8 MiB   @profile
     8                             def fac(n):
     9     13.8 MiB      0.0 MiB       if n == 0:
    10     13.8 MiB      0.0 MiB           return 1
    11     13.8 MiB      0.0 MiB       return fac(n-1) * n


Filename: ~/task_3.pyy

Line #    Mem usage    Increment   Line Contents
================================================
     7     13.8 MiB     13.8 MiB   @profile
     8                             def fac(n):
     9     13.8 MiB      0.0 MiB       if n == 0:
    10     13.8 MiB      0.0 MiB           return 1
    11     13.8 MiB      0.0 MiB       return fac(n-1) * n


6

Вывод: Профилировщик при вызове функции с рекурсией вызывается n+1 раз. Профилирование таким образом не целесообразно. 
Либо при необходимости увеличивать sys.setrecursionlimit.
'''
