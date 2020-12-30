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
    return [i for i, i in enumerate(nums) if i % 2 == 0]


my_arr = [i for i in range(1000)]
print(timeit.timeit('func_1(my_arr)', setup='from __main__ import func_1, my_arr', number=10000))
print(timeit.timeit('func_2(my_arr)', setup='from __main__ import func_2, my_arr', number=10000))
del my_arr

''' Обе функции имеют линейную сложность, но list comprehension раюотает быстрее,
следовательно лучше использовать именно list comprehension.
func_1(my_arr)  # 1.0499413889999687
func_2 my_arr)  # 0.7646469979999893
'''
