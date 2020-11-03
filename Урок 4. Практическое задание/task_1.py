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


def func_my(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


nums_data = [i for i in range(1, 100)]

print(timeit(f"func_1({nums_data})", setup="from __main__ import func_1", number=1000))
print(timeit(f"func_my({nums_data})", setup="from __main__ import func_my", number=1000))

"""
В новой функции использовал генератор списка, получил небольшой прирост. 
"""
