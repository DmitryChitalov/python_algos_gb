"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""

from memory_profiler import profile
import sys

sys.setrecursionlimit(10000)


def seq_sum(nat_num):
    if nat_num == 1:
        return 1
    else:
        return nat_num + seq_sum(nat_num - 1)


@profile
def main():
    inp_num = 9990
    if inp_num * (inp_num + 1) / 2 == seq_sum(inp_num):
        print("Равенство: 1+2+...+n = n(n+1)/2 подтверждается")
    else:
        print("Равенство: 1+2+...+n = n(n+1)/2 НЕ подтверждается")


main()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20     38.4 MiB     38.4 MiB           1   @profile()
    21                                         def main():
    22     38.4 MiB      0.0 MiB           1       inp_num = 9990
    23     42.8 MiB      4.4 MiB           1       if inp_num * (inp_num + 1) / 2 == seq_sum(inp_num):
    24     42.8 MiB      0.0 MiB           1           print("Равенство: 1+2+...+n = n(n+1)/2 подтверждается")
    25                                             else:
    26                                                 print("Равенство: 1+2+...+n = n(n+1)/2 НЕ подтверждается")

Взял рекурсию с задания ко второму уроку. Для избавления от рекурсивного повторения таблиц-профайлеров
поместил тело кода с вызовом рекурсии в другую функцию - main(), и поставил декоратор @profile к ней.
Увеличил глубину рекурсии с целью задействовать побольше памяти: при глубине порядка 10000 задействовалось 4,4 MiB
"""