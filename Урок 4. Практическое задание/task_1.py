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

array = [el for el in range(1, 100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [el for el in nums if el % 2 == 0]


print(timeit("func_1(array)", "from __main__ import func_1, array ", number=1000))
print(timeit("func_2(array)", "from __main__ import func_2, array ", number=1000))

"""
функция func_2() быстрее из за обращения непосредственно к элементу масив а не вызов элемента по индексу как в func_1()
"""
