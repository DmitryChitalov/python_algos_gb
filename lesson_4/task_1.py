"""
Задание 1.
Приведен код, который позволяет сохранить в массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


lst = [i for i in range(randint(1, 100))]

print('func_1:')
print(timeit("func_1(lst)", setup='from __main__ import func_1, lst', number=100000))

print('func_2:')
print(timeit("func_2(lst)", setup='from __main__ import func_2, lst', number=100000))

"""
func_1:
0.9958123
func_2:
0.6615857

func_1:
1.0100154000000001
func_2:
0.6888239999999999

func_2 - функция, использующая генератор списков выигрывает по скорости из-за того у функции, которая использует метод append у списка.

Преподавателя прошу уточнить разницу между "list comprehension" и "генератором списков"
"""
