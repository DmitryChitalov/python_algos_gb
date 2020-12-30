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
    new_arr = []
    index = 0
    for i in nums:
        if i % 2 == 0:
            new_arr.append(index)
        index += 1
    return new_arr


if __name__ == '__main__':
    print(timeit("func_1([41,42,43,45,44,53,34,35,54,67,80,90,97,102])", setup="from __main__ import func_1"))
    print(timeit("func_2([41,42,43,45,44,53,34,35,54,67,80,90,97,102])", setup="from __main__ import func_2"))

'''
Убрала генерацию дополнительного массива и вычисление длины массива заменив на доп переменную и инкремент после каждого цикла
'''
