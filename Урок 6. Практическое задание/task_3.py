"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile
from sys import getsizeof


# @profile
def get_sum(n, my_sum):
    if n > 0:
        my_sum += n
        n -= 1
        return get_sum(n, my_sum)
    else:

        return my_sum


@profile
def run():
    n = 500
    get_sum(n, 0) == int(n * (n + 1) / 2)


if __name__ == '__main__':
    n = 5
    get_sum(n, 0) == int(n * (n + 1) / 2)

"""
Если использовать декоратор "в лоб" то получится что-то вроде:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     19.6 MiB     19.6 MiB           1   @profile
    13                                         def get_sum(n, my_sum):
    14     19.6 MiB      0.0 MiB           1       if n > 0:
    15                                                 my_sum += n
    16                                                 n -= 1
    17                                                 return get_sum(n, my_sum)
    18                                             else:
    19                                         
    20     19.6 MiB      0.0 MiB           1           return my_sum


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     19.6 MiB     19.6 MiB           2   @profile
    13                                         def get_sum(n, my_sum):
    14     19.6 MiB      0.0 MiB           2       if n > 0:
    15     19.6 MiB      0.0 MiB           1           my_sum += n
    16     19.6 MiB      0.0 MiB           1           n -= 1
    17     19.6 MiB      0.0 MiB           1           return get_sum(n, my_sum)
    18                                             else:
    19                                         
    20     19.6 MiB      0.0 MiB           1           return my_sum
    
 Line #    Mem usage    Increment  Occurences   Line Contents
============================================================   
 И т.д.  по количеству вызовов рекурсии, что ни разу не дает нам  представление о потреблении памяти целиком функцией.
Поэтому обернем  рекурсивную функцию в запускающую функцию  и замерим потребление пямяти последней:    
"""

run()
"""
Получаются вполне человекочитаемые данные:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     19.6 MiB     19.6 MiB           1   @profile
    22                                         def run():
    23     19.6 MiB      0.0 MiB           1       n = 500
    24     20.4 MiB      0.8 MiB           1       get_sum(n, 0)==int(n*(n+1)/2)

еще была мысль сделать  рекурсивный счетчик на базе getsizeof, но там простого решения явно не получалось.


Win10x64, Python 3.9.0
"""
