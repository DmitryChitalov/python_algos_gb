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




nums = [2, 3, 4, 5, 6, 4, 5, 7]


def func_2(nums):
    new_arr = [i for i in nums if i % 2 == 0]

    return new_arr


def func_3(nums):
    new_arr1 = list(i for i in nums if i % 2 == 0)
    return new_arr1


print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums"))
print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums"))
print(timeit.timeit("func_3(nums)", setup="from __main__ import func_3, nums"))
"""
я добавила лист ранге и  comprehension  потому что они быстрее чем аппенд, ну у меня comprehension  быстрее чем лист увас было наабарод
"""