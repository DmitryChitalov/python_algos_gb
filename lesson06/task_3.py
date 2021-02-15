"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile

def recursion(n):
    if n == 1:
        return 1
    else:
        return n*recursion(n-1)

@profile
def call_recursion(n):
    return recursion(n)

call_recursion(100)

# Нужно профилировать функцию-обертку, вызывающую рекурсию

# Filename: C:/Users/pavelpe/PycharmProjects/python_algos_gb/lesson06/task_3.py
# #
# # Line #    Mem usage    Increment  Occurences   Line Contents
# # ============================================================
# #     17     18.8 MiB     18.8 MiB           1   @profile
# #     18                                         def call_recursion(n):
# #     19     18.8 MiB      0.0 MiB           1       return recursion(n)
# #
# #
# #
# # Process finished with exit code 0