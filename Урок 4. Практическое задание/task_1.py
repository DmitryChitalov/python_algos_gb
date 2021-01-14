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


nums = [i for i in range(1000)]
print(timeit('func_1(nums)', setup='from __main__ import func_1, nums', number = 100000))

def func_2(nums):
    res = [i for i, y in enumerate(nums) if y % 2 == 0]
    return res

print(timeit('func_2(nums)', setup='from __main__ import func_2, nums', number = 100000))


'''
В результате вычислений получилось
func_1 - 14.995340363
func_2 - 9.512429995

Генераторные выражения работают быстрее, хоть и сложность одинакова O(n)
'''