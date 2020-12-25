"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit, default_timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i]%2==0]


n = range(1000)


print(timeit('func_1(n)','from __main__ import func_1,n', default_timer,10000))
#  Результат - 1.57013608

print(timeit('func_2(n)','from __main__ import func_2,n', default_timer,10000))
# Результат - 1.32634116

# Вторая функция выполняется немного быстрее за счет использования генераторного выражения
