"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
"""Cохранить в массиве индексы четных элементов другого массива"""

from random import randint
from functools import reduce
from memory_profiler import profile


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


num_list = [randint(0, 100) for el in range(1000000)]
print(num_list)
print(func_1(num_list))

"""
Вся память выделяется при создании массива. Дальше новая память не добавляется
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     17.7 MiB     17.7 MiB           1   @profile
    32                                         
    33                                         def func_1(nums):
    34     17.7 MiB      0.0 MiB           1       new_arr = []
    35     17.7 MiB      0.0 MiB          11       for i in range(len(nums)):
    36     17.7 MiB      0.0 MiB          10           if nums[i] % 2 == 0:
    37     17.7 MiB      0.0 MiB           7               new_arr.append(i)
    38     17.7 MiB      0.0 MiB           1       return new_arr

@profile
def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]

num_list = [randint(0, 100) for el in range(10)]
print(num_list)
print(func_2(num_list))
"""
"""
По памяти реализация почти не отличается - память выделяется только при создании массива
Но сложность алгоритма меньше и он выполняется быстрее
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    57     17.6 MiB     17.6 MiB           1   @profile
    58                                         def func_2(nums):
    59     17.7 MiB      0.0 MiB          13       return [i for i, el in enumerate(nums) if el % 2 == 0]
"""
