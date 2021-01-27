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
    return [indx for indx, el in enumerate(nums) if not el % 2]


nums = [el for el in range(1000)]
print(timeit("func_1(nums)", number=10000, globals=globals()))
print(timeit("func_2(nums)", number=10000, globals=globals()))

"""
func_1(nums): 0.6596763280103914
func_2(nums): 0.45932869298849255

Вместо цикла воспользовался list comprehension, для индексации - enumerate. 
Встроенные функции работают быстрее
"""