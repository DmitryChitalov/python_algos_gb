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


""" 1. Цикл for"""

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(func_1([5, 5, 6, 8, 8, 10, 11, 12, 14, 5, 5, 6, 8, 8, 10, 11, 12, 14, 5, 5, 6, 8, 8, 10, 11, 12, 14]))

print(timeit("""
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
"""))


""" 2. Рекурсия"""

def func_2(nums, new_arr=[], i=0):
    if len(nums) == 0:
        return new_arr
    if nums[0] % 2 == 0:
        new_arr.append(i)
    i += 1
    return func_2(nums[1:], new_arr, i)


print(func_2([5, 5, 6, 8, 8, 10, 11, 12, 14, 5, 5, 6, 8, 8, 10, 11, 12, 14, 5, 5, 6, 8, 8, 10, 11, 12, 14]))

print(timeit("""
def func_2(nums, new_arr=[], i=0):
    if len(nums) == 0:
        return new_arr    
    if nums[0] % 2 == 0:
        new_arr.append(i)
    i += 1
    return func_2(nums[1:], new_arr, i)
"""))

""" 3. Генератор списка"""

def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


print(func_3([5, 5, 6, 8, 8, 10, 11, 12, 14, 5, 5, 6, 8, 8, 10, 11, 12, 14, 5, 5, 6, 8, 8, 10, 11, 12, 14]))

print(timeit("""
def func_3(nums):
    return [i for i in range(enumerate(nums)) if nums[i] % 2 == 0]
"""))


""" 1. Цикл for - первоначальная функция"""
""" 2. Рекурсия - работает медленнее"""
""" 3. Генератор списка - работает быстрее всего"""