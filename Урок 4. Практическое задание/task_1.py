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

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def optimization_of_func_1(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0 ]
""""
Генераторное выражение 
уменьшает количество вызовов, тем самым снижается время выполнения программы
"""
nums = [1,2,3,4,5,6,7,8,9]

print(
    timeit.timeit(
        'func_1(nums)',
        setup="from __main__ import func_1, nums",
        number = 1000
    )
)
print(
    timeit.timeit(
        'optimization_of_func_1(nums)',
        setup="from __main__ import optimization_of_func_1, nums",
        number = 1000
    )
)
"""
0.0018174999999999997 func_1
0.0013680000000000012 optimization_of_func_1
"""