"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
"""
Одним из наиболее эффективных вариантов оптимизации ресурсов (в частности, памяти) 
являются ленивые (lazy) вычисления - когда выражение вычисляется в момент первого обращения 
к нему, а не заранее. Как пример можно привести не только вычисление выражений, но и создание 
объектов при первом обращении к ним (что, в общем случае, также является вычислимым выражением), 
и вычислении только в тех случаях когда существующие объекты изменяются.
Генератор в Python является частным случаем ленивых вычислений.

Как видно из приведенных ниже замеров, затраты памяти в случае использования ленивого списка
вместо массива в решете Эратосфена значительно ниже.
Можно еще больше уменьшить затраты памяти, особенно - при хранении многомерных массивов, если хранить
только "ненулевые" элементы массива (по заданному критерию "нуля"), инициализируя по мере необходимости.
Однако, следует заметить, что такие способы оптимизации могут приводить к заметному ухудшению 
производительности.

Введите порядковый номер искомого простого числа: 1000
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     19.3 MiB     19.3 MiB           1   @profile
    55                                         def not_so_simple(in_n):
    56     19.3 MiB      0.0 MiB           1       scr_arr = []
    57     19.3 MiB      0.0 MiB           1       prime_ind = 1
    58     19.3 MiB      0.0 MiB           1       prime = 2
    59     27.2 MiB  -1382.6 MiB     1000002       for i in range(in_n * in_n + 1):
    60     27.2 MiB  -1374.7 MiB     1000001           scr_arr.append(i)
    61     27.2 MiB  -1382.6 MiB     1000001           scr_arr[i] = 0
    62     27.2 MiB      0.0 MiB           1       i = 2
    63     27.2 MiB   -123.7 MiB        7918       while prime_ind <= (in_n):
    64     27.2 MiB   -123.7 MiB        7918           if scr_arr[i] == 0:
    65     27.2 MiB    -15.6 MiB        1000               prime = i
    66     27.2 MiB    -15.6 MiB        1000               if prime_ind == in_n:
    67     27.2 MiB     -0.0 MiB           1                   break
    68     27.2 MiB    -15.6 MiB         999               prime_ind = prime_ind + 1
    69     27.2 MiB    -15.6 MiB         999               j = i * i
    70     27.2 MiB -36289.7 MiB     2123047               while j <= in_n * in_n:
    71     27.2 MiB -36274.1 MiB     2122048                   if scr_arr[j] == 0:
    72     27.2 MiB  -6005.1 MiB      921501                       scr_arr[j] = 1
    73     27.2 MiB -24182.8 MiB     2122048                   j = j + i
    74     27.2 MiB   -131.5 MiB        7917           i += 1
    75     27.2 MiB      0.0 MiB           1       return prime


7919
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     19.6 MiB     19.6 MiB           1   @profile
    35                                         def lazy_not_so_simple(in_n):
    36     19.6 MiB      0.0 MiB           1       scr_arr = LazyZeroList()
    37     19.6 MiB      0.0 MiB           1       prime_ind = 1
    38     19.6 MiB      0.0 MiB           1       prime = 2
    39     19.6 MiB      0.0 MiB           1       i = 2
    40     27.2 MiB      0.0 MiB        7918       while prime_ind <= in_n:
    41     27.2 MiB      0.0 MiB        7918           if scr_arr.getitem(i) == 0:
    42     27.2 MiB      0.0 MiB        1000               prime = i
    43     27.2 MiB      0.0 MiB        1000               if prime_ind == in_n:
    44     27.2 MiB      0.0 MiB           1                   break
    45     27.2 MiB      0.0 MiB         999               prime_ind = prime_ind + 1
    46     27.2 MiB      0.0 MiB         999               j = i * i
    47     27.2 MiB  -3775.4 MiB     2123047               while j <= in_n * in_n:
    48     27.2 MiB  -3767.7 MiB     2122048                   if scr_arr.getitem(j) == 0:
    49     27.2 MiB  -3775.4 MiB      921501                       scr_arr.setitem(j, 1)
    50     27.2 MiB  -3775.4 MiB     2122048                   j = j + i
    51     27.2 MiB      0.0 MiB        7917           i += 1
    52     27.2 MiB      0.0 MiB           1       return prime


7919
"""

from timeit import timeit
from memory_profiler import profile


class LazyZeroList:
    def __init__(self):
        self.data = []

    def getitem(self, index):
        while len(self.data) <= index:
            self.data.append(0)
        return self.data[index]

    def setitem(self, index, value):
        while len(self.data) <= index:
            self.data.append(0)
        self.data[index] = value


@profile
def lazy_not_so_simple(in_n):
    scr_arr = LazyZeroList()
    prime_ind = 1
    prime = 2
    i = 2
    while prime_ind <= in_n:
        if scr_arr.getitem(i) == 0:
            prime = i
            if prime_ind == in_n:
                break
            prime_ind = prime_ind + 1
            j = i * i
            while j <= in_n * in_n:
                if scr_arr.getitem(j) == 0:
                    scr_arr.setitem(j, 1)
                j = j + i
        i += 1
    return prime


@profile
def not_so_simple(in_n):
    scr_arr = []
    prime_ind = 1
    prime = 2
    for i in range(in_n * in_n + 1):
        scr_arr.append(i)
        scr_arr[i] = 0
    i = 2
    while prime_ind <= (in_n):
        if scr_arr[i] == 0:
            prime = i
            if prime_ind == in_n:
                break
            prime_ind = prime_ind + 1
            j = i * i
            while j <= in_n * in_n:
                if scr_arr[j] == 0:
                    scr_arr[j] = 1
                j = j + i
        i += 1
    return prime


i = int(input('Введите порядковый номер искомого простого числа: '))
print(not_so_simple(i))
print(lazy_not_so_simple(i))
print(
    timeit(
        "not_so_simple(i)",
        setup='from __main__ import not_so_simple, i',
        number=1))
print(
    timeit(
        "lazy_not_so_simple(i)",
        setup='from __main__ import lazy_not_so_simple, i',
        number=1))
