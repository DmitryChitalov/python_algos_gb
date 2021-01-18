"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile
import sys

@profile
def task_1():
    for elem in range(100000):
        yield elem


@profile
def task_2_1():
    list1 = []
    for elem in range(100000):
        elem *= 2
        list1.append(elem)
        return list1

@profile
def task_2_2():
    list1 = [el * 2 for el in range(100000)]
    return list1

task_1()
task_2_1()
task_2_2()

print(sys.getsizeof(task_1))
print(sys.getsizeof(task_2_1))
print(sys.getsizeof(task_2_2))
"""
Опять же функция не сработала с yield, мы не храним такие массивы в памяти, а получаем по запросу.

В остальном случае, как ни странно, возможно из-за ошибок работы профайлера, генераторное выражение заняло больше памяти,
чем добавление элемента в список, и работает дольше... память занимается одна и таже для функции"

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     18.6 MiB     18.6 MiB           1   @profile
    17                                         def task_2_1():
    18     18.6 MiB      0.0 MiB           1       list1 = []
    19     18.6 MiB      0.0 MiB           1       for elem in range(100000):
    20     18.6 MiB      0.0 MiB           1           elem *= 2
    21     18.6 MiB      0.0 MiB           1           list1.append(elem)
    22     18.6 MiB      0.0 MiB           1           print(list1)
    23     18.6 MiB      0.0 MiB           1           return list1


[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60...

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    25     18.6 MiB     18.6 MiB           1   @profile
    26                                         def task_2_2():
    27     22.4 MiB      3.9 MiB      100003       list1 = [el * 2 for el in range(100000)]
    28     22.4 MiB     -0.0 MiB           1       print(list1)
    29     22.4 MiB      0.0 MiB           1       return list1
"""