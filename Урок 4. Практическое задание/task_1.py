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

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for el in nums:
        if nums.index(el) % 2 == 0:
            new_arr.append(el)
    return new_arr


def func_3(nums):
    new_arr = nums[::2]
    return new_arr


def func_4(nums):
    new_arr = [x for x in nums if not x % 2]
    return new_arr


print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=10000))
print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=10000))
print(timeit.timeit("func_3(nums)", setup="from __main__ import func_3, nums", number=10000))
print(timeit.timeit("func_4(nums)", setup="from __main__ import func_4, nums", number=10000))

'''Наиболее оптимальным решением данной задачи является формирование нового списка по срезу исходного с шагом 2.
Улучшает показатели вариант решения задачи с помощью генераторной функции по условию.
Аналогичное решение через цикл и встроенные методы списков ухудшило показатели втрое.'''