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


def func_2(nums):
    new_arr = [i for i in nums if not i % 2]
    return new_arr


nums = [i for i in range(1000)]
print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=10000))
print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=10000))

"""
Результаты замеров:
2.4278505000000004
0.9442179999999998

"""