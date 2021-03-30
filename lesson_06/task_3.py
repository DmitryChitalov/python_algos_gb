"""Реализовать замер памяти рекурсивной функции"""

from memory_profiler import profile


@profile
def recursive_func(number):
    def fib_number(num, num_1=0, num_2=1):
        if num <= 3:
            return num_1 + num_2
        summ = num_1 + num_2
        num_1 = num_2
        num_2 = summ
        num -= 1
        return fib_number(num, num_1, num_2)
    return fib_number(number)


recursive_func(10)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      6     18.9 MiB     18.9 MiB           1   @profile
#      7                                         def recursive_func(number):
#      8     18.9 MiB      0.0 MiB           9       def fib_number(num, num_1=0, num_2=1):
#      9     18.9 MiB      0.0 MiB           8           if num <= 3:
#     10     18.9 MiB      0.0 MiB           1               return num_1 + num_2
#     11     18.9 MiB      0.0 MiB           7           summ = num_1 + num_2
#     12     18.9 MiB      0.0 MiB           7           num_1 = num_2
#     13     18.9 MiB      0.0 MiB           7           num_2 = summ
#     14     18.9 MiB      0.0 MiB           7           num -= 1
#     15     18.9 MiB      0.0 MiB           7           return fib_number(num, num_1, num_2)
#     16     18.9 MiB      0.0 MiB           1       return fib_number(number)

# Замеры показывают, что в плане расхода памяти данная функция в оптимизации не нуждается.
