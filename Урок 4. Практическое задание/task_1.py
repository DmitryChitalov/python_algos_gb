"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""


# по сути я переписала первую функцию на генераторное выражение, оно оказалось чуть быстрее


from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


nums = [2, 44, 6, 3, 74, 246, 3, 78, 36, 778, 34, 74, 21, 22, 45, 78, 90, 775, 4]

print(timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1000))


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1000))
