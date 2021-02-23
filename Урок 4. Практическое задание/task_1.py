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

def func_2(nums):
    return [k for k,v in enumerate(nums) if v % 2 == 0]


nums = list(range(100))
print(timeit("func_1(nums)",globals=globals())) # 9.448442400000001
print(timeit("func_2(nums)",globals=globals())) # 6.332066900000001 использовал list-comprehensions т.к. создание нового массива раходует больше времени