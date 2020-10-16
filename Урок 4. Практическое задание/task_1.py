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

# определяем nums
nums = [elem for elem in range(10000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# вторая функция
def func_2(nums):
    return [x for x in nums if not x % 2]


# проверяем работу функции
print(func_1(nums))
print(func_2(nums))

# производим замеры
print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=10000))
print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=10000))

# вторая функция работает быстрее, так как в первой сделана через for и есть append
# функция_1 время 7.469506999999999
# функция_2 время 2.8738190999999995
