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

nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112]


def func_1():
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("func_1()", setup="from __main__ import func_1", number=1000000))


# 1.2296389800030738

def func_2():
    new_arr = []
    for i, _ in enumerate(nums):  # заменил range -> enumerate
        if i % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("func_2()", setup="from __main__ import func_2", number=1000000))


# 1.1097708419983974 - стало быстрее на 0,1 сек

def func_3():
    new_arr = []
    for i in range(0, len(nums), 2):  # при условии, что нужны только чётные элементы то делаем range с шагом 2
        new_arr.append(i)
    return new_arr


print(timeit("func_3()", setup="from __main__ import func_3", number=1000000))
# 0.5302986659953604 - время выполнения уменьшилось в 2 раза
