"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, x in enumerate(nums) if not x % 2]


list = [i for i in range(100)]  # список из 100 элементов
print(timeit(stmt='func_1(list)', globals=globals()))  # 6.0197334 сек.
print(timeit(stmt='func_2(list)', globals=globals()))  # 3.8904815999999993 сек.

""" 
Enumerate работает быстрее, так как в этом случае не нужно
обращаться к элементу по индексу, вместо этого функция сама создаёт
дополнительный счетчик 
"""