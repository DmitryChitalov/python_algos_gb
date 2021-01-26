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
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


nums = list(range(100))
# В комментариях время исполнения:
print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=100000))   # 1.26
print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=100000))   # 0.67


""" Заменил в исходной функции код с циклом на более быстрый код 'list comprehension', 
'list comprehension' оптимизирован для составления коллекций.
 Время исполнения кода сократилось """
