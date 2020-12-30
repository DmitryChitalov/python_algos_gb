"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import timeit, repeat, default_timer

numbers = range(2000)

def func_1(nums : list):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

print(timeit("func_1(numbers)",setup="from __main__ import func_1, numbers",number=1000))
print(repeat("func_1(numbers)",setup="from __main__ import func_1,numbers",timer=default_timer,repeat=3,number=1000))
print(func_1(numbers))  # выводим конечный список

"""Теперь будут замеры для новой, оптимизированной функции, с помощью генераторного выражения"""

def func_1_new(nums: list):
    return [i for i, elem in enumerate(nums) if elem % 2 == 0]

print(timeit("func_1_new(numbers)",setup="from __main__ import func_1_new, numbers",number=1000))
print(repeat("func_1_new(numbers)",setup="from __main__ import func_1_new,numbers",timer=default_timer,repeat=3,number=1000))

"""После повторных замеров использование генераторного выражения 
позволило увличить производительность более чем в 2 раза
Замеры до оптимизации: 0.790405132
Замеры после оптимизации: 0.3264061570000001
"""