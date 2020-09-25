"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
"""
решил попробывать оптимизировать код с помощью генератора списка,
это оказалось правельным решением. В среднем генератор работает в 2 раза быстрее чем цикл.

"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [x for x in nums if x % 2 == 0]


my_list = list(range(1000))

print(timeit.timeit("func_1(my_list)", setup="from __main__ import func_1, my_list", number=10000))
print(timeit.timeit("func_2(my_list)", setup="from __main__ import func_2, my_list", number=10000))

