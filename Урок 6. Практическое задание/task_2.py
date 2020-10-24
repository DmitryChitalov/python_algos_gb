"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile


@profile
def a():
    dicts = {}
    a_str = "Предложите фундаментальные варианты оптимизации памяти и доказать (наглядно, кодом, если получится) их эффективность"
    keys = range(len(a_str))
    values = list(a_str)
    for i in keys:
        dicts[i] = values[i]
    print(dicts)


@profile
def b():
    dicts = {}
    a_str = "Предложите фундаментальные варианты оптимизации памяти и доказать (наглядно, кодом, если получится) их эффективность"
    keys = range(len(a_str))
    values = list(a_str)
    dict(zip(keys, values))
    print(dicts)

@profile
def c():
    a = []
    for i in range(10):
        a.append([1] * (10 ** i))
    return a


@profile()
def c_gen():
    a = []
    a = [([1] * (10 ** i)) for i in range(10)]
    return a


if __name__ == '__main__':
    a()
    b()
    c()
    c_gen()

"""

Видимо я снова взял не удачные примеры:
То, что видно по результату: генераторы и встроенные функции увеличивают быстродействие - т.к. количество 
вхождений сокращается, но при этом память расходуется довольно хорошо в обоих случаях.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    10     12.5 MiB     12.5 MiB           1   @profile
    11                                         def a():
    12     12.5 MiB      0.0 MiB           1       dicts = {}
    13     12.5 MiB      0.0 MiB           1       a_str = "Предложите фундаментальные варианты оптимизации памяти и доказать (наглядно, кодом, если получится) их эффективность"
    14     12.5 MiB      0.0 MiB           1       keys = range(len(a_str))
    15     12.5 MiB      0.0 MiB           1       values = list(a_str)
    16     12.5 MiB      0.0 MiB         117       for i in keys:
    17     12.5 MiB      0.0 MiB         116           dicts[i] = values[i]
    18     12.5 MiB      0.0 MiB           1       print(dicts)



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     12.6 MiB     12.6 MiB           1   @profile
    22                                         def b():
    23     12.6 MiB      0.0 MiB           1       dicts = {}
    24     12.6 MiB      0.0 MiB           1       a_str = "Предложите фундаментальные варианты оптимизации памяти и доказать (наглядно, кодом, если получится) их эффективность"
    25     12.6 MiB      0.0 MiB           1       keys = range(len(a_str))
    26     12.6 MiB      0.0 MiB           1       values = list(a_str)
    27     12.6 MiB      0.0 MiB           1       dict(zip(keys, values))
    28     12.6 MiB      0.0 MiB           1       print(dicts)



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     12.6 MiB     12.6 MiB           1   @profile
    31                                         def c():
    32     12.6 MiB      0.0 MiB           1       a = []
    33   8489.6 MiB      0.0 MiB          11       for i in range(10):
    34   8489.6 MiB   8477.0 MiB          10           a.append([1] * (10 ** i))
    35   8489.6 MiB      0.0 MiB           1       return a



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     97.2 MiB     97.2 MiB           1   @profile()
    39                                         def c_gen():
    40     97.2 MiB      0.0 MiB           1       a = []
    41   8489.6 MiB   8392.3 MiB          13       a = [([1] * (10 ** i)) for i in range(10)]
    42   8489.6 MiB      0.0 MiB           1       return a

"""