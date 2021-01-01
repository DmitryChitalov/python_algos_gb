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
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(i)
    return new_arr


nums = range(1000)


print(timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1000))
print(timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1000))


'''

Время выполнения функций (1000 повторений):

func_1:     0.0015 сек
func_2:     0.0007 сек

В func_2 доступ к элементу по индексу заменен итерированием, что привело к ускорению.

'''
