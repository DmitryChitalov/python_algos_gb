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


def func_1(nums):   # 1.468272733
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):   # 1.208056968
    new_arr = []
    count = 0
    for i in nums:
        if i % 2 == 0:
            new_arr.append(count)
        count += 1
    return new_arr


def func_3(nums, count=0):  # 2.482631836
    if len(nums) == 1:
        if nums[0] % 2 == 0:
            return count
        else:
            return ''
    if nums[0] % 2 == 0:
        return count, func_3(nums[1:], count + 1)
    else:
        return func_3(nums[1:], count + 1)


def start_func():
    a = [44, 55, 66, 77, 88]
    a = func_3(a)
    return a


print(timeit('start_func()', 'from __main__ import start_func'))

# print(start_func())
