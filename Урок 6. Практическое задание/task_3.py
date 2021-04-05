"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile
from random import randint


@profile
def recur(num=2, ret=None):
    if ret is None:
        ret = []
    if num == 0:
        return ret
    return recur(num - 1, ret + [randint(1,100) for i in range(10000)])


recur()
# ---
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     11     39.7 MiB     39.7 MiB           1   @profile
#     12                                         def recur(num=2, ret=None):
#     13     39.7 MiB      0.0 MiB           1       if ret is None:
#     14                                                 ret = []
#     15     39.7 MiB      0.0 MiB           1       if num == 0:
#     16     39.7 MiB      0.0 MiB           1           return ret
#     17                                             return recur(num - 1, ret + [randint(1,100) for i in range(10000)])
#
#
# Filename: /home/erinar/geekbrains/python_algos_gb/Урок 6. Практическое задание/task_3.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     11     39.7 MiB     39.5 MiB           2   @profile
#     12                                         def recur(num=2, ret=None):
#     13     39.7 MiB      0.0 MiB           2       if ret is None:
#     14                                                 ret = []
#     15     39.7 MiB      0.0 MiB           2       if num == 0:
#     16     39.7 MiB      0.0 MiB           1           return ret
#     17     39.7 MiB      0.2 MiB       10003       return recur(num - 1, ret + [randint(1,100) for i in range(10000)])
#
#
# Filename: /home/erinar/geekbrains/python_algos_gb/Урок 6. Практическое задание/task_3.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     11     39.7 MiB     39.5 MiB           3   @profile
#     12                                         def recur(num=2, ret=None):
#     13     39.7 MiB      0.0 MiB           3       if ret is None:
#     14     39.3 MiB      0.0 MiB           1           ret = []
#     15     39.7 MiB      0.0 MiB           3       if num == 0:
#     16     39.7 MiB      0.0 MiB           1           return ret
#     17     39.7 MiB      0.2 MiB       20006       return recur(num - 1, ret + [randint(1,100) for i in range(10000)])
#
# ---
# Видно, что профилировку через memory_profiler для рекурсивных функций
# нельзя делать напрямую


# Сделаем рекурсивную функцию локальной, обернув вокруг нее
# внешнюю функцию
@profile
def wrapped_recur(num=2):
    def recur(num=2, ret=None):
        if ret is None:
            ret = []
        if num == 0:
            return ret
        return recur(num - 1, ret + [randint(1,100) for i in range(10000)])
    return recur()


wrapped_recur()
# ---
# Filename: /home/erinar/geekbrains/python_algos_gb/Урок 6. Практическое задание/task_3.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     21     39.7 MiB     39.7 MiB           1   @profile
#     22                                         def wrapped_recur():
#     23     39.7 MiB      0.0 MiB           4       def recur(num=2, ret=None):
#     24     39.7 MiB      0.0 MiB           3           if ret is None:
#     25     39.7 MiB      0.0 MiB           1               ret = []
#     26     39.7 MiB      0.0 MiB           3           if num == 0:
#     27     39.7 MiB      0.0 MiB           1               return ret
#     28     39.7 MiB      0.0 MiB       20006           return recur(num - 1, ret + [randint(1,100) for i in range(10000)])
#     29     39.7 MiB      0.0 MiB           1       return recur()
#
# ---
#
# Видно, что обернутая функция показывает суммарное потребление памяти
