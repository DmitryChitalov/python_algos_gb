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
import random
arr = [random.randint(1, 1000) for i in range(10000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# В качестве первой оптимизации, я переписала алгоритм, заменив цикл на list comprehension,
# так как эта конструкция работает быстрее циклов.
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# Следующим шагом заменяю доступ по индексу (как правило он медленнее) на перебор элементов с помощью функции enumerate.
def func_3(nums):
    return [i for el, i in enumerate(nums) if el % 2 == 0]


# По замерам стабильно 3 вариант работает быстрее
print(timeit.timeit('func_1(arr)', 'from __main__ import func_1, arr', number=10000))
print(timeit.timeit('func_2(arr)', 'from __main__ import func_2, arr', number=10000))
print(timeit.timeit('func_3(arr)', 'from __main__ import func_3, arr', number=10000))
"""
9.42136161
7.681546156
6.469101219999999
"""

