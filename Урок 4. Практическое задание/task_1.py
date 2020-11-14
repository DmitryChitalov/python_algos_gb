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


lst = [1, 2, 3, 4, 5, 6]

# first way (given example):

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

print(func_1(lst))

res_1 = print(round(timeit('func_1(lst)', setup= 'from __main__ import func_1, lst', number= 10000), 4))


# second way (generator expression + concatenation):

def func_2(nums):
    new_arr = []
    index_even = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    new_arr = new_arr + index_even
    return new_arr

print(func_2(lst))

res_2 = print(round(timeit('func_2(lst)', setup='from __main__ import func_2, lst', number = 10000), 4))


# third way (only gen expression):

def func_3(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

print(func_3(lst))


res_3 = print(round(timeit('func_3(lst)', 'from __main__ import func_3, lst', number = 10000), 4))


# sum up:
'''
Третий способ - только через генераторное выражение - сработал быстрее всех предыдущих, хоть и разница в выполнении
очень мала.
'''

