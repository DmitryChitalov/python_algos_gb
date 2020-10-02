"""
Задание 2.
Предложите еще какие-нибудь варианты (механизмы, библиотеки) оптимизации памяти
и докажите (наглядно, кодом) их эффективность

"""


'''
Варианты, которые были рассмотрены на уроке:
- слоты
- Numpy
- генераторы

Ниже рассматриваем другие варианты.
'''

from memory_profiler import profile


# поздняя загрузка модулей позволяет отложить использование памяти

# import numpy as np

@profile
def my_func():

    a = [i for i in range(100000)]
    del a
    import numpy as np
    a = np.arange(1, 100000, 1).tolist()
    del a


my_func()

'''

загружаем numpy в начале

Line #    Mem usage    Increment   Line Contents
================================================
    23     27.6 MiB     27.6 MiB   @profile
    24                             def my_func():
    25                             
    26     31.8 MiB      0.4 MiB       a = [i for i in range(100000)]
    27     27.6 MiB      0.0 MiB       del a
    28                             
    29     31.8 MiB      4.2 MiB       a = np.arange(1, 100000, 1).tolist()
    30     27.6 MiB      0.0 MiB       del a


загружаем numpy позднее

Line #    Mem usage    Increment   Line Contents
================================================
    24     15.6 MiB     15.6 MiB   @profile
    25                             def my_func():
    26                             
    27     19.6 MiB      0.3 MiB       a = [i for i in range(100000)]
    28     15.6 MiB      0.0 MiB       del a
    29     27.5 MiB     11.9 MiB       import numpy as np  #импорт не в начале модуля в научных целях
    30     31.8 MiB      4.3 MiB       a = np.arange(1, 100000, 1).tolist()
    31     27.6 MiB      0.0 MiB       del a

Мы видим, что загрузка памяти на 11.9 Mib откладывавется до момента, когда модуль непосредственно нужен.

'''


@profile()
def overlaps1(a,b):
    overlaps = []
    for x in a:
        for y in b:
            if x==y:
                overlaps.append(x)

@profile()
def overlaps2(a,b):
    overlaps = set(a) & set(b)


a = [i for i in range(1000)]
b = [i for i in range(500, 1500)]

overlaps1(a,b)
overlaps2(a,b)