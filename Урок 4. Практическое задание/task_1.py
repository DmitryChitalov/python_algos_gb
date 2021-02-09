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
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    even_nums = [i for i in nums if i % 2 == 0]
    return even_nums


var_nums = []
for i in range(10000):
    var_nums.append(randint(1, 100))

print(timeit("func_1(var_nums)", setup="from __main__ import func_1, var_nums",
             number=10000))
print(timeit("func_2(var_nums)", setup="from __main__ import func_2, var_nums",
             number=10000))

#
# 18.5946009
# 8.562831
#
# Вторая функция (через списковое включение) по результатам замеров
# отрабатывает быстрее
#
