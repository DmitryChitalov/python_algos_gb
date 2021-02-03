"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile

@profile
def my_func_gen(u_inp):
    sys_list = [i for i in range(u_inp+1)]
    return sys_list


@profile
def my_func(u_inp):
    sys_list = []
    u_list = range(u_inp+1)
    for i in u_list:
        sys_list.append(i)
    return sys_list

my_func_gen(10000)
my_func(10000)


"""
рассматривая простой пример из первого задания
1/
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    10     17.2 MiB     17.2 MiB           1   @profile
    11                                         def my_func_gen(u_inp):
    12     17.6 MiB      0.4 MiB       10004       sys_list = [i for i in range(u_inp+1)]
    13     17.6 MiB      0.0 MiB           1       return sys_list\

2/
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     17.4 MiB     17.4 MiB           1   @profile
    17                                         def my_func(u_inp):
    18     17.4 MiB      0.0 MiB           1       sys_list = []
    19     17.4 MiB      0.0 MiB           1       u_list = range(u_inp+1)
    20     17.4 MiB      0.0 MiB       10002       for i in u_list:
    21     17.4 MiB      0.0 MiB       10001           sys_list.append(i)
    22     17.4 MiB      0.0 MiB           1       return sys_list


очевидно, что при работе итератора
в первом случае 
экономия памяти в 2 раза -> имеет место быть 
"""