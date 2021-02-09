"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import Timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in nums if (i % 2 == 0)]
    return new_arr


nums = [i for i in range(100)]

print(func_1(nums))
print(func_2(nums))
# print(timeit("func_1(1000)"))
t1 = Timer("func_1(nums)", "from __main__ import func_1, nums")
t2 = Timer("func_2(nums)", "from __main__ import func_2, nums")
print(f"func_1 {t1.timeit(5000)} seconds")
print(f"func_2 {t2.timeit(5000)} seconds")

# Оптимизировал код, применил list comprehension. Производительность функции выросла.
