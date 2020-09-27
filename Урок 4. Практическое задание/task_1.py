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

# Делаем первые замеры


print(timeit("""

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

"""))

# цикл, if да еще и аппенд - это ту мач,
# поэтому используем list comprehension (генераторы, но на самом деле так нельзя переводить же)
# код становится питонистичнее, читабельнее, короче. Ну и, как показывают замеры - немного быстрее.
# но честно говоря, я рассчитываел в более серьезную разницу в скорости.
# максимально у меня получилось 0,082 против 0,069


def func_2(nums):
    new_arr = [num for num in range(len(nums)) if nums[num] % 2 == 0]
    return new_arr


print(timeit("""

def func_2(nums):
    new_arr = [num for num in range(len(nums)) if nums[num] % 2 == 0]
    return new_arr

"""))
