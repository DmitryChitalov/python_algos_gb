"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""


from random import randint
from memory_profiler import profile


#@profile
def recur(number, even=0, odd=0):
    number = int(number)
    if number == 0:
        return print(even, odd)
    my_num = number % 10
    if my_num % 2 == 0:
        even += 1
        return recur(number // 10, even, odd)
    else:
        odd += 1
        return recur(number // 10, even, odd)


@profile
def recur_profile(number):
    recur(number)


recur_profile(randint(100000000000, 9999999999999999999))



"""
Если анализируем "в лоб" рекурсию, то для каждого шага выдает профилировщик:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    14     18.6 MiB     18.6 MiB           1   @profile
    15                                         def recur(number, even=0, odd=0):
    16     18.6 MiB      0.0 MiB           1       number = int(number)
    17     18.6 MiB      0.0 MiB           1       if number == 0:
    18     18.6 MiB      0.0 MiB           1           return print(even, odd)
    19                                             my_num = number % 10
    20                                             if my_num % 2 == 0:
    21                                                 even += 1
    22                                                 return recur(number // 10, even, odd)
    23                                             else:
    24                                                 odd += 1
    25                                                 return recur(number // 10, even, odd)

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    14     18.6 MiB     18.6 MiB           2   @profile
    15                                         def recur(number, even=0, odd=0):
    16     18.6 MiB      0.0 MiB           2       number = int(number)
    17     18.6 MiB      0.0 MiB           2       if number == 0:
    18     18.6 MiB      0.0 MiB           1           return print(even, odd)
    19     18.6 MiB      0.0 MiB           1       my_num = number % 10
    20     18.6 MiB      0.0 MiB           1       if my_num % 2 == 0:
    21     18.6 MiB      0.0 MiB           1           even += 1
    22     18.6 MiB      0.0 MiB           1           return recur(number // 10, even, odd)
    23                                             else:
    24                                                 odd += 1
    25                                                 return recur(number // 10, even, odd)

и т.д.
Можно обернуть выполнение рекурсивной функции в нерекурсивную:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     18.8 MiB     18.8 MiB           1   @profile
    29                                         def recur_profile(number):
    30     18.8 MiB      0.0 MiB           1       recur(number)
И понять, сколько памяти выделяется для выполнения данной функции
"""