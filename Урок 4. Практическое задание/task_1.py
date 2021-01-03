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

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


#print(func_1(nums))

print('Время для 1 функции составило:') ## 0.004379270001663826
print(
    timeit.timeit(
        f"func_1({nums})", setup="from __main__ import func_1", number=1000))


def func_2(nums):
    new_arr_1 = [elem for elem in nums if elem % 2 != 0]
    return new_arr_1


#print(func_2(nums))

print('Время для 2 функции составило:') ## 0.0026921539974864572
print(
    timeit.timeit(
        f"func_2({nums})", setup="from __main__ import func_2", number=1000))


##Благодаря тому что использовали listcomprehension для 2 функции вместо append, удалось оптимизировать код и сократить время.