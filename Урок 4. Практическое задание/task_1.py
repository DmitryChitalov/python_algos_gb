"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

#Оптимизировал решение за счет исползования генератора списков
#Сократилось количество строк с 5 до 1 строки и снизилось время выполнения

"""
(time func_1 number=1000) 0.12044310000000001
(time func_2 number=1000) 0.10155230000000001
(time func_1 number=10000) 1.2791455
(time func_1 number=10000) 1.0918465000000002
"""

def func_2(nums):
    return [el for el in range(len(nums)) if nums[el] % 2 == 0]

nums = [i for i in range(1, 1000)]

print(timeit("func_1(nums)",
             setup="from __main__ import func_1, nums",
             number=1000))


print(timeit("func_2(nums)",
             setup="from __main__ import func_2, nums",
             number=1000))

print(timeit("func_1(nums)",
             setup="from __main__ import func_1, nums",
             number=10000))


print(timeit("func_2(nums)",
             setup="from __main__ import func_2, nums",
             number=10000))
