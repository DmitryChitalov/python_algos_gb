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


LENGTH = 100
test_list = [randint(0, 100) for _ in range(LENGTH)]

print(f"Время выполнения: {timeit('func_1(test_list)', number=100000, globals=globals())}")  # ~ 0.58


# Мы можем переписать реализацию первой функции короче и быстрее по времени выполнения через списковое включение,
# которое уже оптимизировано под создание списков с добавлением элементов по заданному условию:

def func_2(nums):
    return [elem for elem in range(len(nums)) if not nums[elem] % 2]


print(f"Время выполнения: {timeit('func_2(test_list)', number=100000, globals=globals())}")  # ~ 0.43

# Замеры показывают, что вторая функция действительно работает быстрее.
