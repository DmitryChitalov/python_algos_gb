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
    a = [i for i in nums if not i % 2]
    return a

"""
func_2(nums) работает быстрее, 
так как применяется генератор
"""

print(timeit.timeit("func_1([1, 34, 7, 89, 2, 5, 154, 34, 77, 12, 9, 145, 8])", setup="from __main__ import func_1", number = 100000))
print(timeit.timeit("func_2([1, 34, 7, 89, 2, 5, 154, 34, 77, 12, 9, 145, 8])", setup="from __main__ import func_2", number = 100000))

