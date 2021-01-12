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
    new_arr = nums[::2]
    return new_arr


def func_3(nums):
    new_arr = [i for i in nums if not i % 2]
    return new_arr


def func_4(nums):
    new_arr = [i for k, i in enumerate(nums) if not k % 2]
    return new_arr


nums = [i for i in range(1000)]
print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=10000))
print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=10000))
print(timeit.timeit("func_3(nums)", setup="from __main__ import func_3, nums", number=10000))
print(timeit.timeit("func_4(nums)", setup="from __main__ import func_4, nums", number=10000))

"""
1.9957243000000002
0.036350000000000104
0.8569722
1.526421

Сделал еще 3-мя способами, по замерам минимальное время исполнения получается 2м способом.
Оно оптимальное.

"""
