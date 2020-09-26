"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import timeit
my_list = [el for el in range(10000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit.timeit("lambda: func_1(my_list)", setup="from __main__ import func_1", number=10000))


def func_2(nums):
    return [el for el in nums if el % 2]


print(timeit.timeit("lambda: func_2(my_list)", setup="from __main__ import func_2", number=10000))
"""я использовал генератор списка, т.к. он работает быстрее"""

