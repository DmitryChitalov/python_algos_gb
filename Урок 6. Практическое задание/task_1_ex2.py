from memory_profiler import profile
"""
# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
"""


@profile()
def my_func():
    user_list = [el for el in range(500000)]
    index = 0
    for i in range(len(user_list) // 2):
        user_list[index], user_list[index+1] = user_list[index+1], user_list[index]
        index += 2
    return user_list


my_func()

"""
Для запуска программы было выделено 19.5 MiB
Далее для создания списка выделено еще 20.1 MiB
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     9     19.5 MiB     19.5 MiB           1   @profile()
    10                                         def my_func():
    11     39.6 MiB  -2485.5 MiB      500003       user_list = [el for el in range(500000)]
    12     39.6 MiB      0.0 MiB           1       index = 0
    13     39.6 MiB      0.0 MiB      250001       for i in range(len(user_list) // 2):
    14     39.6 MiB      0.0 MiB      250000           user_list[index], user_list[index+1] = user_list[index+1], user_list[index]
    15     39.6 MiB      0.0 MiB      250000           index += 2
    16     39.6 MiB      0.0 MiB           1       return user_list
"""

