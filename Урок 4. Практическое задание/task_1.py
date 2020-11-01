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
    new_arr = [num for num in nums if num% 2 == 0]
    return new_arr

nums = [num for num in range(10)]
print('func_1 cycle - ', timeit("func_1(nums)", setup="from __main__ import func_1, nums"))
print('func_2 list comprehension - ', timeit("func_2(nums)", setup="from __main__ import func_2, nums"))

"""
Вторую функцию сделал через генераторное выражение, т.к. оно выполняется быстрее, чем цикл 
с присоединением новых элементов. Результаты замеров показывают прирост скорости в 1,5 раза.
"""